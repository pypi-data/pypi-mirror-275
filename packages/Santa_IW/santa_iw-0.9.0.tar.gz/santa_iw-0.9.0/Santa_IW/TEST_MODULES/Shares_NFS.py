#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from libsrg.Runner import Runner

from Santa_IW.TestBase import Status, TestBase


# noinspection PyPep8Naming
class Shares_NFS(TestBase):

    def run_test_once(self):
        shares = self.config().get_item("shares")
        expect_set = set(shares)
        self.log_test_status(Status.OK, message=f"Expected {expect_set!r}")
        cmd = ["exportfs", "-s"]
        r = Runner(cmd, userat=self.userat)
        ret = r.ret
        if ret != 0:
            self.log_test_status(Status.UNKNOWN, message=f"Command Error 0x{ret:04x} {r}")
        else:
            lines = r.so_lines
            shared_set = set()
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    shared_set |= {parts[0]}
            missing_set = expect_set - shared_set
            if len(missing_set) > 0:
                self.log_test_status(Status.WARNING, message=f"missing {missing_set} sharing {shared_set}")
            else:
                self.log_test_status(Status.OK, message=f"sharing {shared_set}")


from Santa_IW.TestPluginHelper import TestPluginHelper
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


# noinspection HttpUrlsUsage
class LocalDiscovery(TestDiscoveryBase):

    def discover(self):
        if self.can_ssh:
            r = Runner(f"exportfs -s", userat=self.userat, timeout=5)
            if r.success:
                share_list = [line.split()[0] for line in r.so_lines]
                if len(share_list) > 0:
                    self.add_test(
                        {
                            "test_type": "Shares_NFS",
                            "shares": share_list
                        })

helper = TestPluginHelper(Shares_NFS,LocalDiscovery)
helper.alias("Shares_NFS", {"shares": ["/partimag"],"period":10*TestBase.sc.minute})
