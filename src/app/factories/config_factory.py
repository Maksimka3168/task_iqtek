import os
from abc import abstractmethod, ABC
from typing import Dict

from yaml import load, SafeLoader

from app.models.config import AppConfig


class ConfigFactory:


    @abstractmethod
    def type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_instance(self, filepath: str) -> AppConfig:
        raise NotImplementedError


class YmlConfigFactory(ConfigFactory, ABC):
    def type(self) -> str:
        return "yml"

    def get_instance(self, filepath: str) -> AppConfig:
        with open(filepath, 'r') as f:
            data = load(f, Loader=SafeLoader)
            return AppConfig(
                type=data["type"],
                settings=data["settings"]
            )


class ConfigFactoryStorage:
    def __init__(self):
        self.storage_: Dict[str, ConfigFactory] = {}

    def register_factory(self, factory: ConfigFactory):
        if factory.type() not in self.storage_:
            self.storage_[factory.type()] = factory
        else:
            raise Exception(f"Factory config {factory} already registered")

    def unregister_factory(self, factory: ConfigFactory):
        if factory.type() not in self.storage_:
            del self.storage_[factory.type()]
        else:
            raise Exception(f"Factory config {factory} not registered")

    def get_instance(self, filepath: str) -> AppConfig:
        file_extension = os.path.splitext(filepath)[-1].lower().lstrip('.')
        if file_extension in self.storage_:
            return self.storage_[file_extension].get_instance(filepath=filepath)

        raise Exception(f"Factory config for format .{file_extension} not registered")
