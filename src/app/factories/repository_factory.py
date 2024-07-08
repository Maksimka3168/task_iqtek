from abc import abstractmethod
from functools import partial
from typing import Dict

from adapters.sqlalchemy_db.session import create_session_maker, get_async_session
from repository.base import BaseUserRepository
from repository.database import PostgresUserRepository
from repository.memory import MemoryUserRepository


class RepositoryFactory:

    @abstractmethod
    def type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_instance(self, settings: dict) -> BaseUserRepository:
        raise NotImplementedError


class MemoryRepositoryFactory(RepositoryFactory):

    def type(self) -> str:
        return "memory"

    def get_instance(self, settings: dict) -> BaseUserRepository:
        return MemoryUserRepository()


class PostgresRepositoryFactory(RepositoryFactory):
    def type(self):
        return "postgres"

    def get_instance(self, settings: dict) -> BaseUserRepository:
        session_maker = create_session_maker(settings)
        return PostgresUserRepository(session=partial(get_async_session, session_maker))


class StorageRepositoryFactory:
    def __init__(self):
        self.storage_: Dict[str, RepositoryFactory] = {}

    def register_factory(self, factory: RepositoryFactory):
        if factory.type() not in self.storage_:
            self.storage_[factory.type()] = factory
        else:
            raise Exception("Factory already registered")

    async def unregister_factory(self, factory: RepositoryFactory):
        if factory.type() not in self.storage_:
            del self.storage_[factory.type()]
        else:
            raise Exception("Factory not registered")

    async def get_instance(self, type: str, settings: dict) -> BaseUserRepository:
        if type in self.storage_:
            return self.storage_[type].get_instance(settings=settings)

        raise Exception("Factory not registered")

