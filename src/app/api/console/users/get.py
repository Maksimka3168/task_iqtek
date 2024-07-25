import asyncio

import click

from app.services.users import UserService


class GetUserByIdCommand:

    def __init__(self, service: UserService):
        self.__service = service

    def get_user_by_id(
        self,
        user_id: int,
    ):
        user_info = asyncio.run(self.__service.get(user_id))
        if not user_info:
            click.echo("Пользователь не найден")
        else:
            click.echo(f"Полученный пользователь №{user_info.id} {user_info.full_name}")
