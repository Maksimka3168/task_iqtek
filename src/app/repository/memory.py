from abc import ABC
from typing import Optional

from models.user import User
from repository.base import BaseUserRepository


class MemoryUserRepository(BaseUserRepository, ABC):
    def __init__(self) -> None:
        self.data: list[User] = []

    async def add(self, user: User) -> User:
        user.id = len(self.data) + 1
        self.data.append(user)
        return user

    async def get(self, user_id: int) -> Optional[User]:
        return next((e for e in self.data if e.id == user_id), None)

    async def update(self, user: User) -> Optional[User]:
        self.data = list(map(lambda e: user if e.id == user.id else e, self.data))
        return user

    async def remove(self, user_id: int) -> bool:
        self.data = list(filter(lambda e: e.id != user_id, self.data))
        return True
