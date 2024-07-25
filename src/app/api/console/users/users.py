import click

from app.api.console.users.add import AddUserCommand
from app.api.console.users.delete import DeleteUserByIdCommand
from app.api.console.users.get import GetUserByIdCommand
from app.api.console.users.patch import PatchEditUserByIdCommand
from app.repository.base import BaseUserRepository
from app.services.users import UserService
from app.utils.ioc import ioc


def register_command():
    add_user_command = click.Command(
        name='add_user',
        callback=AddUserCommand(
            service=UserService(
                repository=ioc.get(BaseUserRepository)
            )
        ).add_user,
        params=[
            click.Option(['--full_name'], show_default=True, help='Укажите ФИО Пользователя')
        ]
    )
    remove_user_command = click.Command(
        name='remove_user',
        callback=DeleteUserByIdCommand(
            service=UserService(
                repository=ioc.get(BaseUserRepository)
            )
        ).delete_user_by_id,
        params=[
            click.Option(['--user_id'], show_default=True, help='Укажите ID Удаляемого Пользователя', type=int)
        ]
    )
    get_user_command = click.Command(
        name='get_user',
        callback=GetUserByIdCommand(
            service=UserService(
                repository=ioc.get(BaseUserRepository)
            )
        ).get_user_by_id,
        params=[
            click.Option(['--user_id'], show_default=True, help='Укажите ID Получаемого Пользователя', type=int)
        ]
    )
    edit_user_command = click.Command(
        name='edit_user',
        callback=PatchEditUserByIdCommand(
            service=UserService(
                repository=ioc.get(BaseUserRepository)
            )
        ).edit_user_by_id,
        params=[
            click.Option(['--user_id'], show_default=True, help='Укажите ID Изменяемого Пользователя', type=int),
            click.Option(['--full_name'], show_default=True, help='Укажите Новое ФИО', type=str),
        ]
    )
    group_users = click.Group(
        commands={
            'add': add_user_command,
            'remove': remove_user_command,
            'get': get_user_command,
            'edit': edit_user_command
        }
    )

    return click.Group(
        commands={
            'users': group_users
        }
    )
