#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from libsrg.Runner import Runner

from Santa_IW.TestBase import Status, TestBase


class RemoteProcess(TestBase):

    # def extendParser(self):
    #     self.parser.add_argument("-p", "--proc", action="store", dest="remote_proc",
    #                              default="Mail.app/Contents/MacOS/Mail", help="name of process")

    def run_test_once(self):
        process_name = self.config().get_item("process_name")
        process_user = self.config().get_item("process_user")
        cmd = ["ps", "-fu", process_user]
        r = Runner(cmd, userat=self.userat)
        ret = r.ret
        self.logger.info(ret)
        if ret != 0:
            self.logger.warning(r)
            self.log_test_status(Status.UNKNOWN, message=f"Command Error 0x{ret:04x}")
        else:
            lines = r.so_lines
            for line in lines:
                if process_name in line:
                    self.log_test_status(Status.OK, message=line)
                    break
            else:  # no break
                self.log_test_status(Status.WARNING,
                                     message=f"Process {process_name} for user {process_user} not found")


from Santa_IW.TestPluginHelper import TestPluginHelper
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


# noinspection HttpUrlsUsage
class LocalDiscovery(TestDiscoveryBase):

    def discover(self):
        if not self.can_ssh:
            return
        # I don't see any generic discovery mechanism for this test
        # this one imac happens to run my email triage rules
        if self.fqdn in ["imac.home.goncalo.name"]:
            self.add_test(
                {
                    "test_type": "RemoteProcess",
                    "process_name": "MacOS/Mail",
                    "process_user": "steve",
                    "period": 5 * TestBase.sc.minute
                })
        cmd = ["ps", "-fu", "root"]
        r = Runner(cmd, userat=self.userat)
        if r.success and "/sbin/zed" in r.so_str:
            self.add_test(
                {
                    "test_type": "RemoteProcess",
                    "process_name": "/sbin/zed",
                    "process_user": "root",
                    "period": 5 * TestBase.sc.minute
                })



helper: TestPluginHelper = TestPluginHelper(RemoteProcess, LocalDiscovery)
helper.alias("RemoteProcess",
             {"process_name": "/sbin/zed", "process_user": "root", "period": 5 * TestBase.sc.minute})
