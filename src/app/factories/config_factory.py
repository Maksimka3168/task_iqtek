from abc import abstractmethod, ABC
from typing import Dict

import yaml
from yaml import load


class ConfigFactory:

    @abstractmethod
    async def type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def get_instance(self) -> dict:
        raise NotImplementedError


class YmlConfigFactory(ConfigFactory, ABC):
    async def type(self) -> str:
        return "yml"

    async def get_instance(self) -> dict:
        with open('config.yml', 'r') as f:
            data = load(f, Loader=yaml.SafeLoader)
            return data


class ConfigFactoryStorage:
    def __init__(self):
        self.storage_: Dict[str, ConfigFactory] = {}

    async def register_factory(self, factory: ConfigFactory):
        if await factory.type() not in self.storage_:
            self.storage_[await factory.type()] = factory
        else:
            raise Exception("Factory already registered")

    async def unregister_factory(self, factory: ConfigFactory):
        if await factory.type() not in self.storage_:
            del self.storage_[await factory.type()]
        else:
            raise Exception("Factory not registered")

    async def get_instance(self, type: str) -> dict:
        if type in self.storage_:
            return await self.storage_[type].get_instance()

        raise Exception("Factory not registered")
