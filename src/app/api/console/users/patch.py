import asyncio

import click

from app.models.user import User
from app.services.users import UserService


class PatchEditUserByIdView:

    def __init__(self, service: UserService):
        self.__service = service

    def edit_user_by_id(
        self,
        user_id: int,
        full_name: str,
    ):
        user = User(full_name=full_name)
        user.id = user_id
        asyncio.run(self.__service.update(user))
        click.echo(f"Пользователь №{user_id} успешно отредактирован")
