# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

import logging
import socket
from ipaddress import IPv4Address  # IPv4Network
from pathlib import Path
from typing import Any, Optional, Type

from libsrg.Config import Config
from libsrg.ElapsedTime import ElapsedTime
from libsrg.Runner import Runner

from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


class NodeDiscoveryCandidate:

    def __init__(self, address: IPv4Address, config: Config, group_paths: dict[str, Path], host_template_dir: Path,
                 discovery_classes: list[Type[TestDiscoveryBase]]):
        self.suppress_discovery = None
        self.node_config = None
        self.discovery_classes = discovery_classes
        self.hostname_info = None
        self.is_localhost = None
        self.community = None
        self.map_dev_to_id: dict[str, str] = {}
        self.uname_hostname = "unknown"
        self.kernel_name: str = "unknown"
        self.mac_address: str = "unknown"
        self.oui: str = "unknown"
        self.group_path: Optional[Path] = None
        self.group_name: Optional[str] = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.address = address
        self.config = config
        self.group_paths = group_paths
        self.host_template_dir = host_template_dir
        #
        self.auto_tests: list[dict[str, Any]] = []
        self.auto_templates: list[str] = []
        self.can_ping = False
        self.can_ssh = False
        self.can_name = False
        self.can_snmp = False
        self.overwrite = self.config.get_item("overwrite")
        self.userat = None
        self.short = None
        self.ip_addr_list = None
        self.alias_list = None
        self.fqdn = None
        # self.logger.info(f"Starting {address}")

    def identify(self):
        et = ElapsedTime("identify " + str(self.address))
        self.identify_inner()
        self.logger.debug(f"ElapsedTime {et}")

    def identify_inner(self):
        r = Runner(f"ping -q -c 4 -w 4 -i .25 -W .25 {self.address}", timeout=5, silent=True)
        self.can_ping = r.success
        if not self.can_ping:
            self.logger.debug(f"Can't ping {self.address}")
            return
        self.logger.info(f"Pinged {self.address}")
        try:
            self.fqdn, self.alias_list, self.ip_addr_list = socket.gethostbyaddr(str(self.address))
            self.logger.info(f"Reverse DNS for Address: {self.address} Hostname: {self.fqdn}")
            self.can_name = True
        except socket.herror as e:
            self.logger.error(f"Reverse address lookup failed for {self.address} {e}", stack_info=True, exc_info=True)
        r2 = Runner(f"uname -n", timeout=10, userat=f"root@{self.address}", silent=True)
        self.can_ssh = r2.success
        if r2.success:
            self.uname_hostname = r2.so_lines[0]
        if r2.success and self.fqdn is None:
            self.fqdn = self.uname_hostname
            self.logger.info(f"uname -h for Address: {self.address} Hostname: {self.fqdn}")
            self.can_name = True
        if r2.success and self.fqdn != self.uname_hostname:
            self.logger.warning(
                f"Name conflict for {self.address} Reverse DNS: {self.fqdn} Uname: {self.uname_hostname}")
            self.can_name = False
        if self.fqdn is None:
            self.logger.warning(f"Can't find fqdn/hostname for {self.address}")
            self.can_name = False
            return
        localhost = self.config.get_item("localhost.fqdn")
        self.is_localhost = localhost == self.fqdn

        self.short = self.fqdn.split(".")[0]
        self.userat = f"root@{self.fqdn}"
        r = Runner(f"hostnamectl --json pretty", userat=self.userat, timeout=4, silent=True)
        if r.success:
            self.hostname_info = Config.text_to_config(r.so_str)
            self.logger.info(r)
        r = Runner(f"uname -s", userat=self.userat, timeout=4, silent=True)
        if r.success:
            self.kernel_name = r.so_lines[0].strip()  # "Linux","Darwin"
        else:
            self.kernel_name = "unknown"
        r = Runner(f"arp {self.address}", timeout=4, silent=True)  # localhost not userat
        if r.success:
            for line in r.so_lines:
                parts = line.split()
                if parts[0] == "Address":
                    continue
                if parts[1] == "ether":
                    self.mac_address = parts[2].upper()
                    self.oui = self.mac_address[:8]
                    self.logger.info(f"{self.address=} {self.mac_address=} {self.oui=}")
        self.community = self.config.get_item("__SNMP_COMMUNITY__", secrets=True, default="public")
        cmd = ["snmpget", "-c", self.community, "-v2c", self.fqdn, "-Ovq", "iso.3.6.1.2.1.1.5.0"]
        r = Runner(cmd, timeout=4, silent=True)
        self.can_snmp = r.success

    def create_dev_map(self):
        """Builds a mapping between /dev/sdx and /dev/disk/by-id names"""
        if not self.can_ssh:
            return

        r = Runner("ls -l /dev/disk/by-id/*", userat=self.userat, timeout=4)
        if r.success:
            for line in r.so_lines:
                if "->" in line:
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if part == "->":
                            by_id = parts[i - 1]
                            dev = parts[i + 1].replace("../../", "/dev/")
                            self.map_dev_to_id[dev] = by_id
                            break

    def get_dev_id(self, dev: str)->str:
        """return disk/by_id if found, else dev unchanged"""
        if dev in self.map_dev_to_id:
            return self.map_dev_to_id[dev]
        return dev

    def process_host(self):
        et = ElapsedTime("process_host " + str(self.address))
        self.process_host_inner()
        self.logger.debug(f"ElapsedTime {et}")

    def process_host_inner(self):

        if not (self.can_ping and self.can_name):
            self.logger.debug(f"Skip Processing {self.address} {self.can_name=} {self.can_ping=} {self.can_ssh=}")
            return

        if not self.determine_group():
            self.logger.info(
                f"Skip Processing (no group) {self.address} {self.can_name=} {self.can_ping=} {self.can_ssh=}")
            return

        # self.logger.info(f"Start Processing {self.address} {self.can_name=} {self.can_ping=} {self.can_ssh=}")

        self.create_dev_map()

        self.write_host_file()
        self.write_host_template()
        self.logger.info(f"End Processing {self.address} {self.can_name=} {self.can_ping=} {self.can_ssh=}")

    def determine_group(self) -> bool:
        # lst = self.config.to_list()
        # self.logger.info(lst)
        if self.kernel_name in self.config:
            self.group_name = self.config.get_item(self.kernel_name)
        else:
            self.logger.error(f"Can't find group for {self.kernel_name}, dropping {self.address} {self.fqdn}")
            return False

        self.logger.info(f"{self.address} {self.short} assigned group {self.group_name}")
        explicit_group_assignments = Config(self.config.get_item("explicit_group_assignments", default={}))
        group_name_init = self.group_name
        self.logger.info(f"searching {str(self.address)=}, {self.short=}, {self.mac_address=}, {self.oui=}")
        group_name_new = explicit_group_assignments.get_item(str(self.address), self.short, self.mac_address, self.oui,
                                                             default=group_name_init)
        if group_name_init != group_name_new:
            self.group_name = group_name_new
            self.logger.info(f"{self.address} {self.short} group reassigned {group_name_init} -> {self.group_name}")

        if self.group_name in self.group_paths:
            self.group_path = self.group_paths[self.group_name]
        else:
            if self.group_name.lower().startswith(("drop", "!")):
                self.logger.warning(f"Group {self.group_name}, dropping {self.address} {self.short}")
                return False
            self.logger.error(f"Group {self.group_name} does not exist, dropping {self.address} {self.short}")
            return False
        return True

    def write_host_file(self):
        host_file_path: Path = self.group_path / f"{self.fqdn}.json"
        if host_file_path.exists() and not self.overwrite:
            self.logger.warning(f"Host file {host_file_path} is already exists -- not overwriting")
            return
        additional_tests = Config(self.config.get_item("additional_per_node", "additional_tests", default={}))
        data = additional_tests.get_item(str(self.address), self.short, self.mac_address, self.oui, default={})

        ncon = Config(data)
        self.node_config=ncon
        self.suppress_discovery=ncon.get_item("suppress_discovery", default=[])
        ncon.set_item("fqdn", self.fqdn)
        ncon.set_item("discovered_ipv4", str(self.address))
        if self.mac_address != "unknown":
            ncon.set_item("discovered_mac", str(self.mac_address))
            ncon.set_item("discovered_oui", str(self.oui))
        ncon.set_item("can_ping", self.can_ping)
        ncon.set_item("can_ssh", self.can_ssh)
        ncon.set_item("can_name", self.can_name)
        ncon.set_item("can_snmp", self.can_snmp)
        ncon.set_item("kernel_name", self.kernel_name)

        ncon.set_item("short_name", self.short)
        templates = ncon.get_item("templates", default=[])
        templates.append(f"auto_{self.fqdn}")
        ncon.set_item("templates", templates)
        ncon.to_json_file(host_file_path, indent=4)
        self.logger.info(f"Host config for {self.fqdn} added at {host_file_path}")

    def add_test(self, d: dict[str, Any]):
        test_type=d.get("test_type",None)
        if test_type and test_type not in self.suppress_discovery:
            self.auto_tests.append(d)
            self.logger.info(f"{self.short} Adding test {len(self.auto_tests)} {d} ")
        else:
            self.logger.warning(f"{self.short} suppressed test {len(self.auto_tests)} {d} ")

    def add_template(self, d: str):
        self.auto_templates.append(d)
        self.logger.info(f"{self.short} Adding template {len(self.auto_templates)} {d} ")

    def write_host_template(self):
        auto_file_path: Path = self.host_template_dir / f"auto_{self.fqdn}.json"
        if auto_file_path.exists() and not self.overwrite:
            self.logger.warning(f"Host file {auto_file_path} is already exists -- not overwriting")
            return
        ncon = Config()

        for cls in self.discovery_classes:
            try:
                obj = cls(self)
                obj.discover()
            except Exception as e:
                self.logger.error(f"Exception while adding {cls} : {e}")

        ncon.set_item("intended_for", self.fqdn)
        ncon.set_item("tests", self.auto_tests)
        ncon.set_item("templates", self.auto_templates)
        ncon.to_json_file(auto_file_path, indent=4)
        self.logger.info(f"Host template for {self.fqdn} added at {auto_file_path}")
