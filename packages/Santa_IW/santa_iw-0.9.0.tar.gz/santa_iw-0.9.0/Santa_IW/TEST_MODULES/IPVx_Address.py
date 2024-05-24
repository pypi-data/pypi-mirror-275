#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

import re

from libsrg.Config import Config
from libsrg.Runner import Runner

from Santa_IW.TestBase import Status, TestBase


# noinspection PyPep8Naming
class IPVx_Address(TestBase):

    def run_test_once(self):
        scope = self.config().get_item("scope", default="global")  # link
        inet = self.config().get_item("inet", default="inet")  # inet6
        cmd = ["ip", "-oneline", "addr"]
        self.logger.info(cmd)
        r = Runner(cmd, userat=self.userat)
        ret = r.ret
        self.logger.info(ret)
        r2 = Runner("ip r", userat=self.userat)
        dev="unk"
        if r2.success:
            route = r2.so_lines[0]
            for line in r2.so_lines:
                self.log_test_status(Status.OK, line)
        else:
            route = " no route"
        if ret != 0:
            self.log_test_status(Status.UNKNOWN, message=f"Command Error 0x{ret:04x}")
        else:
            lines = r.so_lines
            # 2: enp1s0    inet 10.0.4.80/16 brd 10.0.255.255 scope global dynamic noprefixroute enp1s0\       valid_lft 3436sec preferred_lft 3436sec
            for line in lines:
                if "deprecated" in line:
                    continue
                if re.match("1:\\slo\\s", line):
                    continue

                if not re.search(r"\s" + inet + r"\s", line):
                    continue
                if not re.search("scope\\s" + scope + "\\s", line):
                    continue
                parts = line.split()
                addr=parts[3]
                dev=parts[1]
                self.log_test_status(Status.OK, tag=f"{parts[3]:<20} {route}")
                break
            else:
                self.log_test_status(Status.NODATA, message=f'no match for {inet}')
                return
            rn=Runner(f"nmcli device show {dev}", userat=self.userat)
            if rn.success:
                con=Config.text_to_config(rn.so_str)
                if inet == "inet":
                    addresses= [value for key, value in con.items() if "ip4.address" in key]
                    dns = [value for key, value in con.items() if "ip4.dns" in key]
                    routes = [value for key, value in con.items() if "ip4.route" in key]
                else:
                    addresses= [value for key, value in con.items() if "ip6.address" in key]
                    dns = [value for key, value in con.items() if "ip6.dns" in key]
                    routes = [value for key, value in con.items() if "ip6.route" in key]
                for key,value in con.items():
                    self.log_test_status(Status.OK, tag=f"{key}:{value}")
                self.log_test_status(Status.OK, message=f"{self.parent().short_name():<20} {dev:<10} A {','.join(addresses)} DNS {','.join(dns)}")
            else:
                self.log_test_status(Status.OK, message=f"{self.parent().short_name():<20} {dev:<10} A {addr} no nmcli")


from Santa_IW.TestPluginHelper import TestPluginHelper
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


class LocalDiscovery(TestDiscoveryBase):

    def discover(self):
        if self.can_ssh and self.kernel_name=="Linux":
            self.add_test(
                {
                    "test_type": "IPV4_Address"
                })
            self.add_test(
                {
                    "test_type": "IPV6_Address"
                })


helper: TestPluginHelper = TestPluginHelper(IPVx_Address, LocalDiscovery)
helper.alias("IPV4_Address", {"scope": "global", "inet": "inet", "period": 5 * TestBase.sc.minute})
helper.alias("IPV6_Address", {"scope": "global", "inet": "inet6", "period": 5 * TestBase.sc.minute})
