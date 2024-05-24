#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from libsrg.Config import Config
from libsrg.Runner import Runner
from libsrg.Statistics.AnalogStatsSlidingWindow import AnalogStatsSlidingWindow

from Santa_IW.Subassembly import Subassembly
from Santa_IW.TestBase import Status, TestBase


class DiskFree(TestBase):

    def __init__(self, instance_config: Config, short_name: str, parent: Subassembly, stepparent: Subassembly):
        super().__init__(instance_config=instance_config, parent=parent, stepparent=stepparent,
                         short_name=short_name)  # super defines self.logger
        # self.ttl_stats = AnalogStatsFading(self.prefix_name("Ping_ms"))
        # self.miss_stats = AnalogStatsFading(self.prefix_name("ReplyRatio"))
        self.used_stats = AnalogStatsSlidingWindow(self.prefix_name("PercentUsed"))

    def run_test_once(self):
        warn_t = self.config().get_item("warning")
        crit_t = self.config().get_item("critical")
        path = self.config().get_item("path")
        cmd = [
            "df", path, "--output=pcent,size,used,avail,file,target"]
        r = Runner(cmd, userat=self.userat)

        ret = r.ret
        self.logger.info(ret)
        if ret != 0:
            self.log_test_status(Status.UNKNOWN, message=f"Command Error 0x{ret:04x} {path}")
        else:
            lines = r.so_lines
            if len(lines) != 2:
                self.log_test_status(Status.UNKNOWN, message=f"Expected 2 lines in {lines}")
            else:
                line = lines[-1].strip()
                parts = line.split(' ')
                self.logger.info("Split")
                n = 6
                if len(parts) < n:
                    self.logger.warning(parts)
                    self.log_test_status(Status.UNKNOWN, message=f"Expected {n} parts in {line}")
                else:
                    val = (parts[0])[:-1]
                    self.logger.info(val)
                    used = float(val)
                    msg = f"Used {used:6.2f}% on {path}"
                    self.used_stats.sample(used)
                    if used > crit_t:
                        self.log_test_status(Status.CRITICAL, message=msg)
                    elif used > warn_t:
                        self.log_test_status(Status.WARNING, message=msg)
                    else:
                        self.log_test_status(Status.OK, message=msg)


from Santa_IW.TestPluginHelper import TestPluginHelper
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


# noinspection HttpUrlsUsage
class LocalDiscovery(TestDiscoveryBase):

    def discover(self):
        if self.can_ssh:
            r = Runner(f"cat /etc/fstab", userat=self.userat, timeout=5)
            if r.success:
                # #
                # # /etc/fstab
                # # Created by anaconda on Thu Mar 14 21:16:25 2024
                # #
                # # Accessible filesystems, by reference, are maintained under '/dev/disk/'.
                # # See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info.
                # #
                # # After editing this file, run 'systemctl daemon-reload' to update systemd
                # # units generated from this file.
                # #
                # /dev/mapper/rhel_kylo-root /                       xfs     defaults        0 0
                # UUID=abf33b68-bf8c-4a55-8189-98d9ec34e699 /boot                   xfs     defaults        0 0
                # UUID=925A-976A          /boot/efi               vfat    umask=0077,shortname=winnt 0 2
                # /dev/mapper/rhel_kylo-home /home                   xfs     defaults        0 0
                # /dev/mapper/rhel_kylo-swap none                    swap    defaults        0 0
                for line in r.so_lines:
                    if line.startswith(("#", ";")):
                        continue
                    parts = line.split()
                    if len(parts) >= 2:
                        path = parts[1]
                        fs = parts[2]
                        path.strip()
                        if path in ["none", "/proc", "swap"]:
                            continue
                        if fs in ["swap","nfs","nfs4","smb"]:
                            continue
                        instance_name = path.replace("/", "_")
                        cmd = {
                            "test_type": "DiskFree",
                            "path": path,
                            "instance_name": instance_name
                        }
                        self.add_test(cmd)


helper: TestPluginHelper = TestPluginHelper(DiskFree,LocalDiscovery)
helper.alias("DiskFree", {"warning": 75, "critical": 80,"period":10*TestBase.sc.minute})
