#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from datetime import datetime
from datetime import timedelta

from libsrg.Config import Config
from libsrg.Runner import Runner
from libsrg.Statistics.AnalogStatsFading import AnalogStatsFading

from Santa_IW.Subassembly import Subassembly
from Santa_IW.TestBase import Status, TestBase


# noinspection PyPep8Naming
class ZFS_Snapshots(TestBase):

    def __init__(self, instance_config: Config, short_name: str, parent: Subassembly, stepparent: Subassembly):
        super().__init__(instance_config=instance_config, parent=parent, stepparent=stepparent,
                         short_name=short_name)  # super defines self.logger
        self.vol: str = self.config().get_item("vol", "pool", "dev", "par_0")
        self.warnS = self.config().get_item("warnS", default=45)
        self.critS = self.config().get_item("critS", default=90)
        self.age = AnalogStatsFading(self.prefix_name("ageSeconds"))
        self.snapshots = AnalogStatsFading(self.prefix_name("snapshotsCount"))

    # def extendParser(self):
    #
    #     self.parser.add_argument("-C", "--critical",
    #                              action="store", dest="critS", default=60, help="critical age threshold in minutes",
    #                              type=int)
    #     self.parser.add_argument("-W", "--warning",
    #                              action="store", dest="warnS", default=25, help="warning age threshold in minutes",
    #                              type=int)
    #     self.parser.add_argument("-V", "--volume",
    #                              action="store", dest="vol", default="ZRaid/PRIMARY/NFSPUB/GPUB",
    #                              help="full name of device (ex /dev/sda)")

    def run_test_once(self):
        zargs = ["/sbin/zfs", "list", "-H", "-t",
                 "snapshot", "-r",
                 "-d1", "-o", "name,creation", "-S", "creation", self.vol]
        r = Runner(zargs, userat=self.userat)
        lines = r.so_lines
        ret = r.ret
        if ret != 0:
            res_str = f"UNKNOWN - Command Error 0x{ret:04x} {self.vol}"
            self.log_test_status(Status.UNKNOWN, message=res_str)
        else:
            minutes = 60
            warn_t = timedelta(0, minutes * int(self.warnS))
            crit_t = timedelta(0, minutes * int(self.critS))

            # reg=re.compile(r'auto-([-0-9:_.]*)')
            # regp=re.compile(r'[-:_.]+')
            dtnow = datetime.now()
            if lines:
                nlines = len(lines)
                for line in lines:
                    parts = line.split('\t')
                    self.logger.info(parts)
                    name = parts[0]
                    if len(parts) > 1:
                        dat_a = parts[1]
                        dt = datetime.strptime(dat_a, '%a %b %d %H:%M %Y')
                        age = dtnow - dt
                        self.age.sample(age.total_seconds())
                        self.snapshots.sample(nlines)
                        if age >= crit_t:
                            res_str = f"CRITICAL - Age {age} for {name} of {nlines}"
                            self.log_test_status(Status.CRITICAL, message=res_str)
                        elif age > warn_t:
                            res_str = f"WARNING - Age {age} for {name} of {nlines}"
                            self.log_test_status(Status.WARNING, message=res_str)
                        elif nlines > 500:
                            res_str = f"WARNING - Age {age} for {name} of {nlines}>500"
                            self.log_test_status(Status.WARNING, message=res_str)
                        else:
                            res_str = f"OK - Age {age} for {name} of {nlines}"
                            self.log_test_status(Status.OK, message=res_str)
                        break
            else:
                res_str = f"CRITICAL - No snapshots for {self.vol}"
                self.log_test_status(Status.CRITICAL, message=res_str)


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
        zfs_volumes_processed = []
        r = Runner("cat /etc/pyznap/pyznap.conf", userat=self.userat, timeout=4)
        if r.success:
            data = Config(Config.text_to_dict('\n'.join(r.so_lines)))
            for vol_name in data.keys():
                sdata = data[vol_name]
                if sdata.get("snap", "no") == "yes":
                    cmd = {
                        "par_0": vol_name,
                        "test_type": "ZFS_Snapshots_Primary"
                    }
                    self.add_test(cmd)
                    zfs_volumes_processed.append(vol_name)
        r = Runner("zfs list -H -o name", userat=self.userat, timeout=10)
        zfs_volumes = r.so_lines
        for vol_name in zfs_volumes:
            # Looking for vols with no child vols
            matched = False
            for vol_name2 in zfs_volumes:
                if vol_name == vol_name2:
                    continue
                if vol_name2.startswith(vol_name):
                    matched = True
                    break
            if matched:
                continue
            if vol_name in zfs_volumes_processed:
                continue
            if not self.check_age_of_snapshots(vol_name):
                continue
            cmd = {
                "par_0": vol_name,
                "test_type": "ZFS_Snapshots_Copy"
            }
            self.add_test(cmd)
            zfs_volumes_processed.append(vol_name)


    def check_age_of_snapshots(self, vol) -> bool:
        zfs_commands = ["/sbin/zfs", "list", "-H", "-t",
                        "snapshot", "-r",
                        "-d1", "-o", "name,creation", "-S", "creation", vol]
        r = Runner(zfs_commands, userat=self.userat, timeout=15)
        lines = r.so_lines
        ret = r.ret
        if ret != 0:
            res_str = f"UNKNOWN - Command Error 0x{ret:04x} {vol}"
            self.logger.warning(res_str)
            return False
        else:
            minutes = 60
            crit_t = timedelta(0, minutes * 60)

            datetime_now = datetime.now()
            if lines:
                for line in lines:
                    parts = line.split('\t')
                    self.logger.info(parts)
                    # name = parts[0]
                    if len(parts) > 1:
                        dat_a = parts[1]
                        dt = datetime.strptime(dat_a, '%a %b %d %H:%M %Y')
                        age = datetime_now - dt
                        self.logger.info(f"Snapshot {vol} age {age} minutes")
                        return age <= crit_t
        return False


helper: TestPluginHelper = TestPluginHelper(ZFS_Snapshots,LocalDiscovery)
helper.alias("ZFS_Snapshots_Primary", {"warnS": 15, "critS": 30, "period": 10 * TestBase.sc.minute})
helper.alias("ZFS_Snapshots_Copy", {"warnS": 45, "critS": 90, "period": 10 * TestBase.sc.minute})
