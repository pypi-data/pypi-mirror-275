# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

import logging
import os
from concurrent.futures import ThreadPoolExecutor
from ipaddress import IPv4Address, IPv4Network  # IPv4Network
from pathlib import Path
from typing import Any, Type

from libsrg.Config import Config
from libsrg.ElapsedTime import ElapsedTime
from libsrg.Info import Info
from libsrg.Runner import Runner

from Santa_IW.NodeDiscoveryCandidate import NodeDiscoveryCandidate
from Santa_IW.NorthPole import NorthPole
from Santa_IW.PluginBase import PluginBase
from Santa_IW.PluginType import PluginType
from Santa_IW.Status import Status
from Santa_IW.Subassembly import Subassembly
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


class MakeListsEmbedded:

    def __init__(self, santa_config: Config, np: NorthPole):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.np = np
        self.santa_config = santa_config
        self.candidate_hosts: list[NodeDiscoveryCandidate] = []
        self.group_path_dict: dict[str, Path] = dict()
        self.is_root = os.getuid() == 0

        self.test_factory= santa_config.get_item("test_factory")
        self.discovery_classes:list[Type[TestDiscoveryBase]] = self.test_factory.get_test_discovery_classes()

        if not self.np.santa_discovery_config_dir.exists():
            self.np.create_discovery_dirs()

        self.logger.info(f"Santa_IW config output to {self.np.santa_discovery_config_dir}")

        self.logger.info(f"Santa_IW discovery input config is {self.np.user_discovery_file}")
        self.info = Info()
        self.localhost_config = self.info.to_config("localhost.")
        self.discovery_config = Config(self.np.user_discovery_file, self.localhost_config)

        self.worker_pool = ThreadPoolExecutor(max_workers=32)  # fixme config

        self.create_dirs()
        self.loop_over_scans()
        #

    def create_dirs(self) -> None:
        # create group subdirectories below HOST_NODES
        groups: dict[str, Any] = self.discovery_config.get_item("groups")
        for group, group_config in groups.items():
            # if the given group name contains a slash "HOSTS/RPI"
            # this will magically create nested groups
            # group_short is just the last part of this name
            group_short = group.split('/')[-1]
            path = self.np.santa_discovery_nodes_dir / group
            path.mkdir(parents=True, exist_ok=True)
            self.group_path_dict[group] = path
            # data in config should just reflect th last part of this name
            con = Config(dict({
                "short_name": group_short,
                "tests": [],
                "templates": []
            }), group_config)

            con.to_json_file(path / f'__{group_short}.json', indent=4)
            self.logger.info(f"Santa_IW group path {group} at {path}")

    def loop_over_scans(self):
        scan_defaults = self.discovery_config.get_item("scan_defaults")
        scans = self.discovery_config.get_item("scans")
        for scan in scans:
            scan_config = Config(scan, scan_defaults, self.discovery_config)
            self.perform_one_scan(scan_config)

        self.logger.info(f"Phase one, identify hosts")
        futures = [self.worker_pool.submit(candidate.identify) for candidate in self.candidate_hosts]
        for future in futures:
            future.result()
        self.logger.info(f"Phase two, process hosts")
        futures = [self.worker_pool.submit(candidate.process_host) for candidate in self.candidate_hosts if
                   candidate.can_ping]
        for future in futures:
            future.result()

    def perform_one_scan(self, scan_config: Config):
        first_ip = scan_config.get_item("first_ip")
        last_ip = scan_config.get_item("last_ip")
        if first_ip.lower() == "auto":
            local_info = Info("localhost")
            r = Runner("ip -oneline addr", timeout=5)
            for line in r.so_lines:
                if local_info.ip in line:
                    # 2: enp0s31f6    inet 10.0.4.32/24 brd 10.0.4.255 scope global dynamic noprefixroute enp0s31f6\       valid_lft 3076sec preferred_lft 3076sec
                    parts = line.split()
                    cidr_range = parts[3]
                    break
            else:
                self.logger.error(f"Could not find ip address {local_info.ip} in {r.so_lines}")
                exit(1)
            network = IPv4Network(cidr_range, strict=False)
            net_addr_start = network.network_address
            net_addr_end = network.broadcast_address
            int_net_addr_start = self.ipv4_to_int(net_addr_start) + 1
            int_net_addr_end = self.ipv4_to_int(net_addr_end) - 1
            # given huge range, limit to x.y.0.1 through x.y.4.254
            int_net_addr_end = min(int_net_addr_end, int_net_addr_start + (5 * 256) - 3)
            first_address = IPv4Address(int_net_addr_start)
            last_address = IPv4Address(int_net_addr_end)
            self.logger.info(f"Santa_IW auto will scan {first_address} -> {last_address}")
        else:
            first_address = IPv4Address(first_ip)
            last_address = IPv4Address(last_ip)
        self.logger.info(
            f"{first_address=} {first_address.packed=} {first_address.compressed=} {last_address.exploded=} {last_address.version=}")
        first_int = self.ipv4_to_int(first_address)
        last_int = self.ipv4_to_int(last_address)
        num = last_int - first_int
        self.logger.info(f"Scanning {num=} addresses {first_address=} {last_address=}")
        for int_addr in range(first_int, last_int + 1):
            ip = IPv4Address(int_addr)
            self.logger.info(f"Scanning {ip=} {int_addr=:x}")
            x = NodeDiscoveryCandidate(address=ip, config=scan_config,
                                       host_template_dir=self.np.santa_discovery_templates_dir,
                                       group_paths=self.group_path_dict,
                                       discovery_classes=self.discovery_classes)
            self.candidate_hosts.append(x)

    # noinspection PyMethodMayBeStatic
    def ipv4_to_int(self, ipv4: IPv4Address) -> int:
        byts = ipv4.packed
        v: int = 0
        for byte in byts:
            v = v * 256 + byte
        return v


# noinspection DuplicatedCode
class Discovery(Subassembly):

    def __init__(self, instance_config: Config, short_name: str, parent: Subassembly):
        super().__init__(instance_config=instance_config, parent=parent,
                         short_name=short_name)  # super defines self.logger
        self.plugin_type_map: dict[str, PluginType] = {}
        self.plugin_instance_map: dict[str, PluginBase] = {}
        self.plugin_names_not_found: set[str] = set()
        # failure within a test type does not imply factory failure
        self._propagate_child_stats_in_overall = False
        self.np = NorthPole()

    def start(self) -> None:
        # fixme add rotation later
        if self.np.santa_discovery_config_dir.is_dir():
            self.log_internal_status(Status.OK,
                                     message=f"Keeping Previous Network Discovery at {self.np.santa_discovery_config_dir}")
        else:
            et = ElapsedTime("discovery")
            self.log_internal_status(Status.OK, message="Performing network discovery")
            _ = MakeListsEmbedded(self.config(), self.np)
            et.stop()
            self.log_internal_status(Status.OK, message=f"Net discovery completed {et}")

    def report(self) -> str:
        out = super().report()
        out += "\n"
        return out
