from api.users.schemas import UserCreate
from models.user import User
from utils.core.ioc import ioc


class PostAddUserView:

    async def add_user(
        self,
        user_create: UserCreate,
    ):
        repository = ioc.repository
        user_info = await repository.add(User(
            full_name=user_create.full_name
        ))
        return user_info