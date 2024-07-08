import os

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


def create_session_maker(settings: dict):

    DATABASE_URL = f"{settings['driver']}://{settings['username']}:{settings['password']}@{settings['hostname']}/{settings['database_name']}"

    engine = create_async_engine(DATABASE_URL)
    return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session(session_maker: sessionmaker) -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session
