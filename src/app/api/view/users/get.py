from repository.base import BaseUserRepository
from utils.core.ioc import ioc


class GetUserByIdView:

    async def get_user_by_id(
        self,
        user_id: int,
    ):
        repository = ioc.get(BaseUserRepository)
        return await repository.get(user_id)
