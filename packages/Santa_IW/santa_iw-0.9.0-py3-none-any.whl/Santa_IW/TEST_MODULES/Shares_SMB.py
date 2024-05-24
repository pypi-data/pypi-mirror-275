#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from libsrg.Runner import Runner

from Santa_IW.TestBase import Status, TestBase


# noinspection PyPep8Naming
class Shares_SMB(TestBase):

    def run_test_once(self):
        """
        Test SMB shares from localhost. Compares set of shares seen with set expected.

        uses smb_username and smb_passwd from secrets area if provided, so avoid logging raw command.

        """
        smb_username = self.config().get_item("smb_username", secrets=True, default=None, allow_none=True)
        smb_password = self.config().get_item("smb_password", secrets=True, default=None, allow_none=True)
        shares = self.config().get_item("shares")
        expect_set = set(shares)
        self.log_test_status(Status.OK, message=f"Expected {expect_set!r}")

        # Note: smbclient command runs on localhost, no userat needed
        if smb_username and smb_password:
            r = Runner(f"smbclient -L  {self.fqdn} -U {smb_username} --password {smb_password}", timeout=5, silent=True)
        else:
            r = Runner(f"smbclient -L  {self.fqdn}", timeout=5)

        ret = r.ret
        self.logger.info(r)
        if ret != 0:
            self.log_test_status(Status.UNKNOWN, message=f"Command Error 0x{ret:04x}")
        else:
            lines = r.so_lines
            shared_set = set()
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    if parts[1] == "Disk":
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
            smb_username = self.config.get_item("__SECRET__SMB_USER", secrets=True, default=None, allow_none=True)
            smb_password = self.config.get_item("__SECRET__SMB_PASS", secrets=True, default=None, allow_none=True)
            if smb_username and smb_password:
                r = Runner(f"smbclient -L  {self.fqdn} -U {smb_username} --password {smb_password}", timeout=5)
            else:
                r = Runner(f"smbclient -L  {self.fqdn}", timeout=5)
            if r.success:
                share_list = [line.strip().split()[0] for line in r.so_lines if "Disk" in line]
                if smb_username and smb_password:
                    self.add_test(
                        {
                            "test_type": "Shares_SMB",
                            "shares": share_list,
                            "smb_username": "{{__SECRET__SMB_USER}}",
                            "smb_password": "{{__SECRET__SMB_PASS}}",
                        })
                else:
                    self.add_test(
                        {
                            "test_type": "Shares_SMB",
                            "shares": share_list,
                        })


helper = TestPluginHelper(Shares_SMB,LocalDiscovery)
helper.alias("Shares_SMB", period=10 * TestBase.sc.minute
             )
