#!/usr/bin/env  python3
# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from libsrg.Runner import Runner

from Santa_IW.TestBase import Status, TestBase


# noinspection PyPep8Naming
class SNMP_id(TestBase):

    # def extendParser(self):
    #     pass
    #     # can set thresholds to allow known count of uncorrectable errors if needed

    def run_test_once(self):

        community = self.config().get_item("community", secrets=True)

        cmd0 = ["snmpwalk", "-c", community, "-v2c", self.fqdn, "-Ovq", ]
        oids = ["iso.3.6.1.2.1.47.1.1.1.1.2",
                "iso.3.6.1.2.1.47.1.1.1.1.10", "iso.3.6.1.2.1.47.1.1.1.1.11",
                "iso.3.6.1.2.1.47.1.1.1.1.13", "iso.3.6.1.2.1.1.5.0"]

        out2 = ""
        for oid in oids:
            cmd = cmd0.copy()
            cmd.append(oid)
            r = Runner(cmd, silent=True)
            ret = r.ret
            self.logger.info(ret)
            if ret != 0:
                self.log_test_status(Status.NODATA, message=f"{oid=} Command Error 0x{ret:04x}")
            else:
                lines = r.so_lines
                for line in lines:
                    sline = line.strip('"\n')
                    self.log_test_status(Status.OK, sline)
                    n = len(sline)
                    if (n < 4) or (n > 30) or (sline.startswith("Slot")) or sline.startswith(
                            "Broadcom") or sline.startswith("Stack") or sline.startswith("switch processor"):
                        continue
                    self.logger.info(sline)
                    out2 = out2 + sline + " "
        self.log_test_status(Status.OK, message=out2)


from Santa_IW.TestPluginHelper import TestPluginHelper
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


class SNMPDiscovery(TestDiscoveryBase):

    def discover(self):
        if not self.can_snmp:
            return
        self.add_test(
            {
                "test_type": "SNMP_id",
                "community": "{{__SNMP_COMMUNITY__}}",
            })


helper: TestPluginHelper = TestPluginHelper(SNMP_id, SNMPDiscovery)
helper.alias("SNMP_id", {"period": 15 * TestBase.sc.minute, "community": "public"})
