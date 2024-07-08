from abc import abstractmethod, ABC
from typing import Dict

import yaml
from yaml import load


class ConfigFactory:

    @abstractmethod
    def type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_instance(self) -> dict:
        raise NotImplementedError


class YmlConfigFactory(ConfigFactory, ABC):
    def type(self) -> str:
        return "yml"

    def get_instance(self) -> dict:
        with open('config.yml', 'r') as f:
            data = load(f, Loader=yaml.SafeLoader)
            return data


class ConfigFactoryStorage:
    def __init__(self):
        self.storage_: Dict[str, ConfigFactory] = {}

    def register_factory(self, factory: ConfigFactory):
        if factory.type() not in self.storage_:
            self.storage_[factory.type()] = factory
        else:
            raise Exception("Factory already registered")

    def unregister_factory(self, factory: ConfigFactory):
        if factory.type() not in self.storage_:
            del self.storage_[factory.type()]
        else:
            raise Exception("Factory not registered")

    def get_instance(self, type: str) -> dict:
        if type in self.storage_:
            return self.storage_[type].get_instance()

        raise Exception("Factory not registered")
