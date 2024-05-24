#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from libsrg.Runner import Runner

from Santa_IW.TestBase import Status, TestBase


# noinspection PyPep8Naming
class ZFS_Version(TestBase):

    # def extendParser(self):
    #     pass
    #     # can set thresholds to allow known count of uncorrectable errors if needed

    def run_test_once(self):
        cmd = ["zfs", "--version"]
        self.logger.info(cmd)
        r = Runner(cmd, userat=self.userat)
        ret = r.ret
        self.logger.info(ret)
        if ret == 127:
            self.log_test_status(Status.OK, message="zfs not found")
        elif ret != 0:
            self.log_test_status(Status.UNKNOWN, message=f"Command Error 0x{ret:04x}")
        else:
            lines = r.so_lines
            self.logger.info(lines)
            first = lines[0]

            self.log_test_status(Status.OK, message=first)


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


        cmd = {
            "test_type": "ZFS_Version",
            "period": 900
        }
        self.add_test(cmd)


helper: TestPluginHelper = TestPluginHelper(ZFS_Version, LocalDiscovery)
helper.alias("ZFS_Version", period=1 * TestBase.sc.hour)
