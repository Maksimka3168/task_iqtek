import asyncio

import click

from app.models.user import User
from app.services.users import UserService


class AddUserCommand:

    def __init__(self, service: UserService):
        self.__service = service

    def add_user(
            self,
            full_name: str
    ):
        user_info = asyncio.run(self.__service.add(User(
            full_name=full_name
        )))
        click.echo(f'Пользователь №{user_info.id} {user_info.full_name} успешно добавлен')
