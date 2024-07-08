from repository.base import BaseUserRepository
from utils.core.ioc import ioc


class DeleteUserByIdView:

    async def delete_user_by_id(
        self,
        user_id: int,
    ):
        repository = ioc.get(BaseUserRepository)
        return await repository.remove(user_id)
