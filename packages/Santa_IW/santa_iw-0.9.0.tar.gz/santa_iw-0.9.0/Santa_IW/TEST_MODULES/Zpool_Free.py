#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from libsrg.Config import Config
from libsrg.Runner import Runner
from libsrg.Statistics.AnalogStatsFading import AnalogStatsFading

from Santa_IW.Subassembly import Subassembly
from Santa_IW.TestBase import Status, TestBase


# noinspection PyPep8Naming
class Zpool_Free(TestBase):

    def __init__(self, instance_config: Config, short_name: str, parent: Subassembly, stepparent: Subassembly):
        super().__init__(instance_config=instance_config, parent=parent, stepparent=stepparent,
                         short_name=short_name)  # super defines self.logger
        self.percent_used = AnalogStatsFading(self.prefix_name("percent_used"))

    # def extendParser(self):
    #     self.parser.add_argument("-p", "--pool", action="store", dest="pool", default="ZRaid", help="Name of pool")
    #     self.parser.add_argument("-C", "--critical", action="store", dest="critS", default=90,
    #                              help="critical % capacity used", type=int)
    #     self.parser.add_argument("-W", "--warning", action="store", dest="warnS", default=86,
    #                              help="warning % capacity used", type=int)

    def run_test_once(self):
        warn_t = float(self.config().get_item("warnS", default=86))
        crit_t = float(self.config().get_item("critS", default=90))
        pool = self.config().get_item("pool")

        cmd = ["/sbin/zpool", "get", "capacity", "-pH", pool]
        self.logger.info(cmd)
        r = Runner(cmd, userat=self.userat)
        ret = r.ret
        self.logger.info(ret)
        if ret != 0:
            self.log_test_status(Status.UNKNOWN, message=f"Command Error 0x{ret:04x} {pool}")
        else:
            lines = r.so_lines
            parts = lines[0].split('\t')
            self.logger.info("Split")
            if len(parts) != 4:
                self.log_test_status(Status.UNKNOWN, message=f"Expected 4 parts in {lines[0]}")
            else:
                self.logger.info(parts[2])
                used = int(parts[2])
                self.percent_used.sample(used)
                if used > crit_t:
                    self.log_test_status(Status.CRITICAL, message=f"Used {used}% {pool}")
                elif used > warn_t:
                    self.log_test_status(Status.WARNING, message=f"Used {used}% {pool}")
                else:
                    self.log_test_status(Status.OK, message=f"Used {used}% {pool}")


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
                "test_type": "Zpool_Status",
                "instance_name": pool_name,
                "period": 300,
                "pool": pool_name
            }
            self.add_test(cmd)


helper = TestPluginHelper(Zpool_Free,LocalDiscovery)
helper.alias("Zpool_Free", period=15 * TestBase.sc.minute)
