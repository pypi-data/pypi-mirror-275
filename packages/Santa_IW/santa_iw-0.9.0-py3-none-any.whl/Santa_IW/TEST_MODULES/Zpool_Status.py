#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from datetime import datetime

from libsrg.Config import Config
from libsrg.Runner import Runner
from libsrg.Statistics.AnalogStatsFading import AnalogStatsFading

from Santa_IW.Subassembly import Subassembly
from Santa_IW.TestBase import Status, TestBase


# noinspection PyPep8Naming
class Zpool_Status(TestBase):

    def __init__(self, instance_config: Config, short_name: str, parent: Subassembly, stepparent: Subassembly):
        super().__init__(instance_config=instance_config, parent=parent, stepparent=stepparent,
                         short_name=short_name)  # super defines self.logger
        self.run_hours = AnalogStatsFading(self.prefix_name("PowerOnHours"))
        self.pool: str = self.config().get_item("pool", "dev", "par_0")

    # def extendParser(self):
    #     self.parser.add_argument("-p", "--pool", action="store", dest="pool",
    #     default="ZRaid", help="Name of ZFS Pool")

    def run_test_once(self):

        cmd = ["zpool", "status", self.pool]
        self.logger.info(cmd)
        r = Runner(cmd, userat=self.userat)
        ret = r.ret
        self.logger.info(ret)

        lines = r.so_lines

        out2 = f"{self.pool} "
        state = ""
        scan = ""

        for line in lines:
            ls = line.strip()
            if ls.startswith("state:"):
                state = ls.split(" ")[-1]
                out2 = out2 + state + " "
            if ls.startswith("scan:"):
                scan = ls[-20:]
                out2 = out2 + "scanned " + scan + " "
            if ls.startswith("errors:"):
                errs = ls[8:]
                out2 = out2 + errs + " "

        if scan != "":
            scandate = datetime.strptime(scan, "%b %d %H:%M:%S %Y")
            now = datetime.now()
            age = now - scandate
            if age.days > 10:
                out2 += f"Scan aged {age.days} days"
                self.log_test_status(Status.WARNING, message=out2)

        # process return code
        if ret >= 127:
            self.log_test_status(Status.CRITICAL, message=out2)
        elif ret >= 1:
            self.log_test_status(Status.CRITICAL, message=out2)
        elif ret < 0:
            self.log_test_status(Status.WARNING, message=out2)
        else:
            self.log_test_status(Status.OK, message=out2)

        # process state
        if "DEGRADED" in state:
            self.log_test_status(Status.WARNING, message=out2)
        elif "FAULTED" in state:
            self.log_test_status(Status.CRITICAL, message=out2)
        elif "ONLINE" in state:
            self.log_test_status(Status.OK, message=out2)
        else:
            self.log_test_status(Status.UNKNOWN, message=out2)


from Santa_IW.TestPluginHelper import TestPluginHelper
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


# noinspection HttpUrlsUsage
class LocalDiscovery(TestDiscoveryBase):

    def discover(self):
        if not self.can_ssh:
            return
        r = Runner("zpool list -H -o name", userat=self.userat, timeout=10)
        if not r.success:
            return
        for pool_name in r.so_lines:

            cmd = {
                "test_type": "Zpool_Free",
                "instance_name": pool_name,
                "period": 300,
                "pool": pool_name
            }
            self.add_test(cmd)

helper = TestPluginHelper(Zpool_Status,LocalDiscovery)
helper.alias("Zpool_Status", period=10 * TestBase.sc.minute)
