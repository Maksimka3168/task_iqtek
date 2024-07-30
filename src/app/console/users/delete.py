import asyncio

import click

from app.services.users import UserService


class DeleteUserByIdCommand:

    def __init__(self, service: UserService):
        self.__service = service

    def delete_user_by_id(
        self,
        user_id: int,
    ):
        users_remove_response = asyncio.run(
            self.__service.remove(user_id)
        )
        if users_remove_response:
            click.echo('Пользователь был успешно удалён.')
        else:
            click.echo('Пользователь Не был удалён по ошибке.')
