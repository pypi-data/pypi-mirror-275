#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

import plistlib
from datetime import datetime
from pathlib import Path

from libsrg.Config import Config
from libsrg.Runner import Runner
from libsrg.Statistics.AnalogStatsFading import AnalogStatsFading

from Santa_IW.Subassembly import Subassembly
from Santa_IW.TestBase import Status, TestBase


# /TM_MACOS/TM_IMAC/imac.sparsebundle
# ls *.plist
# com.apple.TimeMachine.MachineID.plist  com.apple.TimeMachine.SnapshotHistory.plist  Info.plist

class TimeMachine(TestBase):

    def __init__(self, instance_config: Config, short_name: str, parent: Subassembly, stepparent: Subassembly):
        super().__init__(instance_config=instance_config, parent=parent, stepparent=stepparent,
                         short_name=short_name)  # super defines self.logger
        self.snapshot_age = AnalogStatsFading(self.prefix_name("Age_Days"))
        self.snapshot_count = AnalogStatsFading(self.prefix_name("Snapshots"))

    def plist_as_dict(self, name, bundle):
        fpath = bundle / name
        cmd = ["cat", str(fpath)]
        r = Runner(cmd, rethrow=True, verbose=True, userat=self.userat)
        pdict = plistlib.loads(r.so_bytes)
        self.log_test_status(Status.NODATA, f"{fpath} {pdict!r}")
        return pdict

    def run_test_once(self):
        warn_t = self.config().get_item("warning_threshold_days")
        crit_t = self.config().get_item("critical_threshold_days")
        path = self.config().get_item("path")
        r = Runner(f"ls {path}/*bundle -d", userat=self.userat)
        subs = r.so_lines
        self.logger.info(subs)
        if len(subs) < 1:
            self.log_test_status(Status.CRITICAL, message=f"*bundle not found in {path}")
        elif len(subs) > 1:
            self.log_test_status(Status.CRITICAL, message=f"MULTIPLE {subs} found in {path}")
        bpath = Path(subs[0])

        pdict = self.plist_as_dict("com.apple.TimeMachine.MachineID.plist", bpath)
        bdict = self.plist_as_dict("com.apple.TimeMachine.SnapshotHistory.plist", bpath)
        # idict = self.plist_as_dict("Info.plist", bpath)

        model_id = pdict["com.apple.backupd.ModelID"]
        backup = pdict['VerificationDate']
        # tz = backup.tzinfo # there was not tz info
        now = datetime.utcnow()
        age = now - backup
        age_days = age.total_seconds() / self.sc.day

        snaps = bdict["Snapshots"]
        nsnaps = len(snaps)
        if nsnaps > 0:
            last = snaps[-1]
            self.logger.info(last)
            when = last.get('com.apple.backupd.SnapshotCompletionDate', "???")
            # siz = last.get('com.apple.backupd.SnapshotTotalBytesCopied', -10)
            # isize = idict.get('size', -10)
            age = now - when
            age_days = age.total_seconds() / self.sc.day

        else:
            when = "?"
            # siz = -1
            # isize = -2

        self.snapshot_age.sample(age_days)
        self.snapshot_count.sample(nsnaps)
        msg = f"age {age} {bpath} snaps={nsnaps} {model_id} {when}"
        self.logger.info(msg)
        if age_days > crit_t:
            self.log_test_status(Status.CRITICAL, message=msg)
        elif age_days > warn_t:
            self.log_test_status(Status.WARNING, message=msg)
        else:
            self.log_test_status(Status.OK, message=msg)


from Santa_IW.TestPluginHelper import TestPluginHelper
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


# noinspection HttpUrlsUsage
class LocalDiscovery(TestDiscoveryBase):

    def discover(self):
        if not self.can_ssh:
            return
        r = Runner("zfs list -H -o mountpoint", userat=self.userat, timeout=10)
        if not r.success:
            return
        for line in r.so_lines:
            r2 = Runner(f"ls {line}/*bundle/com.apple.TimeMachine.MachineID.plist", userat=self.userat,
                        timeout=10)
            pth = Path(line)
            nam = Path(pth.name).name
            if r2.success:
                cmd = {
                    "test_type": "TimeMachine",
                    "path": line,
                    "instance_name": nam
                }
                self.add_test(cmd)


helper: TestPluginHelper = TestPluginHelper(TimeMachine, LocalDiscovery)
# no default for path
helper.alias("TimeMachine", {"warning_threshold_days": 14, "critical_threshold_days": 21},
             period=30 * TestBase.sc.minute)
