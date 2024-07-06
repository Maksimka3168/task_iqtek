from abc import ABC, abstractmethod
from typing import Optional
from models.user import User


class BaseUserRepository(ABC):
    @abstractmethod
    async def add(self, user: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def remove(self, user_id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, user: User) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def get(self, user_id: int) -> Optional[User]:
        raise NotImplementedError()
