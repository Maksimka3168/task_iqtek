from abc import abstractmethod
from functools import partial
from typing import Dict, Mapping, Any

from app.adapters.sqlalchemy_db.session import create_session_maker, get_async_session
from app.models.settings import PostgresSetting
from app.repository.base import BaseUserRepository
from app.repository.database import PostgresUserRepository
from app.repository.memory import MemoryUserRepository


class RepositoryFactory:

    @abstractmethod
    def type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_instance(self, settings: Mapping[str, Any]) -> BaseUserRepository:
        raise NotImplementedError


class MemoryRepositoryFactory(RepositoryFactory):

    def type(self) -> str:
        return "memory"

    def get_instance(self, settings: Mapping[str, Any]) -> BaseUserRepository:
        return MemoryUserRepository()


class PostgresRepositoryFactory(RepositoryFactory):
    def type(self):
        return "postgres"

    def get_instance(self, settings: Mapping[str, Any]) -> BaseUserRepository:
        required_keys = {
            'driver': str,
            'username': str,
            'password': str,
            'hostname': str,
            'database_name': str
        }
        for key, expected_type in required_keys.items():
            if key not in settings:
                raise ValueError(f'Missing required setting for postgres: {key}')
            if not isinstance(settings[key], expected_type):
                raise TypeError(
                    f'Invalid type for {key}: expected {expected_type.__name__}, got {type(settings[key]).__name__}')
        session_maker = create_session_maker(PostgresSetting(
            driver=settings.get("driver"),
            username=settings.get("driver"),
            password=settings.get("password"),
            hostname=settings.get("hostname"),
            database_name=settings.get("database_name")
        ))
        return PostgresUserRepository(session=partial(get_async_session, session_maker))


class StorageRepositoryFactory:
    def __init__(self):
        self.storage_: Dict[str, RepositoryFactory] = {}

    def register_factory(self, factory: RepositoryFactory):
        if factory.type() not in self.storage_:
            self.storage_[factory.type()] = factory
        else:
            raise Exception(f"Factory repository {factory} already registered")

    def unregister_factory(self, factory: RepositoryFactory):
        if factory.type() not in self.storage_:
            del self.storage_[factory.type()]
        else:
            raise Exception(f"Factory repository {factory} not registered")

    def get_instance(self, type: str, settings: Mapping[str, Any]) -> BaseUserRepository:
        if type in self.storage_:
            return self.storage_[type].get_instance(settings=settings)

        raise Exception(f"Factory repository with type {type} not registered")
