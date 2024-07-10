from api.users.schemas import UserCreate
from models.user import User
from repository.base import BaseUserRepository
from utils.core.ioc import ioc


class PostAddUserView:

    def __init__(self, repository: BaseUserRepository):
        self.__repository = repository

    async def add_user(
            self,
            user_create: UserCreate,
    ):
        user_info = await self.__repository.add(User(
            full_name=user_create.full_name
        ))
        return user_info
