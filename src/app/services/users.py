from typing import Optional

from app.models.user import User
from app.repository.base import BaseUserRepository


class UserService:
    def __init__(self, repository: BaseUserRepository):
        self.__repository = repository

    async def add(self, user: User) -> User:
        if await self.__repository.get_by_name(user.full_name):
            raise Exception("User already exists")
        return await self.__repository.add(user)

    async def remove(self, user_id: int) -> bool:
        if not await self.__repository.get(user_id):
            raise Exception("There is no such user")
        return await self.__repository.remove(user_id)

    async def update(self, user: User) -> bool:
        return await self.__repository.update(user)

    async def get(self, user_id: int) -> Optional[User]:
        return await self.__repository.get(user_id)
