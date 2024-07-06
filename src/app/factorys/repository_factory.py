from abc import abstractmethod
from functools import partial
from typing import Dict

from adapters.sqlalchemy_db.session import create_session_maker, get_async_session
from repository.base import BaseUserRepository
from repository.database import PostgresUserRepository
from repository.memory import MemoryUserRepository


class RepositoryFactory:

    @abstractmethod
    async def type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def get_instance(self, settings: dict) -> BaseUserRepository:
        raise NotImplementedError


class RepositoryMemoryFactory(RepositoryFactory):

    async def type(self) -> str:
        return "memory"

    async def get_instance(self, settings: dict) -> BaseUserRepository:
        return MemoryUserRepository()


class RepositoryPostgresFactory(RepositoryFactory):
    async def type(self):
        return "postgres"

    async def get_instance(self, settings: dict) -> BaseUserRepository:
        session_maker = await create_session_maker()
        return PostgresUserRepository(session=partial(get_async_session, session_maker))


class RepositoryFactoryStorage:
    def __init__(self):
        self.storage_: Dict[str, RepositoryFactory] = {}

    async def register_factory(self, factory: RepositoryFactory):
        if await factory.type() not in self.storage_:
            self.storage_[await factory.type()] = factory

        raise Exception("Factory already registered")

    async def unregister_factory(self, factory: RepositoryFactory):
        if await factory.type() not in self.storage_:
            del self.storage_[await factory.type()]

        raise Exception("Factory not registered")

    async def get_instance(self, type: str, settings: dict) -> BaseUserRepository:
        if type in self.storage_:
            return await self.storage_[type].get_instance(settings=settings)

        raise Exception("Factory not registered")

