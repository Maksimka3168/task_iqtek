from app.api.gateway.users.schemas import UserCreate
from app.models.user import User
from app.services.users import UserService


class PostAddUserView:

    def __init__(self, service: UserService):
        self.__service = service

    async def add_user(
            self,
            user_create: UserCreate,
    ):
        user_info = await self.__service.add(User(
            full_name=user_create.full_name
        ))
        return user_info
