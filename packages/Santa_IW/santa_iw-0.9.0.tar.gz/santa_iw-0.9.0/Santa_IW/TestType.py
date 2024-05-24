# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

from typing import Type

from libsrg.Config import Config

from Santa_IW.Node import Node
from Santa_IW.Subassembly import Subassembly
from Santa_IW.TestBase import TestBase


class TestType(Node):
    def __init__(self, instance_config: Config, short_name: str, parent: Subassembly,
                 test_class: Type[TestBase]) -> None:
        super().__init__(instance_config=instance_config, parent=parent,
                         short_name=short_name,sw_node=True)  # super defines self.logger
        self._test_class = test_class
        self._pull_up_child_annotation = True

    def get_test_class(self) -> Type[TestBase]:
        return self._test_class
