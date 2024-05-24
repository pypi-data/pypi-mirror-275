# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

import logging
from typing import Type, Optional, Any

from libsrg.Config import Config

from Santa_IW.TestBase import TestBase
from Santa_IW.TestDiscoveryBase import TestDiscoveryBase


class TestPluginHelper:
    def __init__(self, loaded_class: Type[TestBase],
                 discovery_class: Type[TestDiscoveryBase]):
        self.logger = logging.getLogger(__name__)
        self._loaded_class = loaded_class
        self._discovery_class = discovery_class
        self._aliases: list[str] = []
        self._configs: dict[str, Config] = {}

    def alias(self, name: str, config: Optional[dict[str, Any] | Config] = None, **overrides) -> Config:
        """
        Allows TestFactory to create a test_type which can create a new instance of the test class with supplied config.
        Config is copied before storing it, so changes do not affect other test_types.
        Any overrides given will change the config defaults.

        :param name: The name of the "test_type" created
        :param config: The default configuration settings for the test_type
        :param overrides: zero or more changes to the config as passed in
        :return: A copy of the default configuration, including overrides
        """
        self._aliases.append(name)
        new_config = Config(config) if config is not None else Config({})
        self._configs[name] = new_config
        for k, v in overrides.items():
            new_config[k] = v

        return new_config.copy()

    def get_all_configs(self) -> dict[str, Config]:
        if not self._aliases:
            self.alias(self._loaded_class.__name__, {})
        return self._configs

    def get_loaded_class(self) -> Type[TestBase]:
        return self._loaded_class

    def get_discovery_class(self) -> Type[TestDiscoveryBase]:
        return self._discovery_class
