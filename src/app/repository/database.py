from abc import ABC
from typing import Optional

from sqlalchemy import select, insert, update, delete

from models.user import User, UserResponse
from repository.base import BaseUserRepository

from adapters.sqlalchemy_db.models import Users


class PostgresUserRepository(BaseUserRepository, ABC):

    def __init__(self, session):
        self.session = session

    async def add(self, user: User) -> User:
        query = (
            insert(Users)
            .values(
                full_name=user.full_name
            )
            .returning(Users)
        )
        result = await self.session.execute(query)
        await self.session.commit()
        user_info = result.scalar()
        return UserResponse(
            id=user_info.id,
            full_name=user_info.full_name
        )

    async def get(self, user_id: int) -> Optional[User]:
        query = (
            select(Users)
            .where(
                Users.id == user_id
            )
        )
        result = await self.session.execute(query)
        user_info = result.scalar()
        if not user_info:
            return
        return UserResponse(
            id=user_info.id,
            full_name=user_info.full_name
        )

    async def update(self, user: User) -> Optional[User]:
        query = (
            update(Users)
            .where(Users.id == user.id)
            .values(full_name=user.full_name)
        )
        await self.session.execute(query)
        await self.session.commit()
        return user

    async def remove(self, user_id: int) -> bool:
        query = (
            delete(Users)
            .where(Users.id == user_id)
        )
        await self.session.execute(query)
        await self.session.commit()
        return True
