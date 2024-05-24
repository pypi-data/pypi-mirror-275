# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from abc import ABC, abstractmethod
from typing import Any


# NodeDiscoveryCandidate can not be included here without going circular
class TestDiscoveryBase(ABC):
    def __init__(self, host_creator):
        self.host_creator = host_creator
        self.config = self.host_creator.config
        self.logger = self.host_creator.logger
        self.fqdn = self.host_creator.fqdn
        self.can_ping = self.host_creator.can_ping
        self.can_ssh = self.host_creator.can_ssh
        self.can_name = self.host_creator.can_name
        self.userat = self.host_creator.userat
        self.can_snmp = self.host_creator.can_snmp
        self.is_localhost = self.host_creator.is_localhost
        self.kernel_name = self.host_creator.kernel_name

    def add_test(self, d: dict[str, Any]):
        self.host_creator.add_test(d)

    def add_template(self, d: str):
        self.host_creator.add_template(d)

    def get_dev_id(self, dev_name) -> str:
        return self.host_creator.get_dev_id(dev_name)

    @abstractmethod
    def discover(self):
        pass
