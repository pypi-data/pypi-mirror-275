#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from libsrg.Runner import Runner

from Santa_IW.TestBase import Status, TestBase


# noinspection PyPep8Naming
class SE_Status(TestBase):

    def run_test_once(self):
        cmd = ["sestatus"]
        self.logger.info(cmd)
        r = Runner(cmd, userat=self.userat)
        ret = r.ret
        self.logger.info(ret)
        if ret == 127:
            self.log_test_status(Status.OK, message="NA")
        elif ret != 0:
            self.log_test_status(Status.UNKNOWN, message=f"Command Error 0x{ret:04x}")
        else:
            lines = r.so_lines
            ena = "UNKNOWN"
            mode = "NA"
            for line in lines:
                parts = line.split(':')
                if parts[0] == "SELinux status":
                    ena = parts[1].strip()
                if parts[0] == "Current mode":
                    mode = parts[1].strip()

            if ena == "enabled":
                self.log_test_status(Status.OK, message=f"{ena} {mode}")
            else:
                self.log_test_status(Status.OK, message=f"{ena}")


from Santa_IW.TestPluginHelper import TestPluginHelper
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


# noinspection HttpUrlsUsage
class LocalDiscovery(TestDiscoveryBase):

    def discover(self):
        if self.can_ssh and self.kernel_name == "Linux":
            r = Runner(f"sestatus", userat=self.userat, timeout=5)
            if r.success:
                self.add_test({"test_type": "SE_Status"})


helper: TestPluginHelper = TestPluginHelper(SE_Status, LocalDiscovery)
helper.alias("SE_Status", period=30 * TestBase.sc.minute)
