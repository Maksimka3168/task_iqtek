from repository.base import BaseUserRepository


class DeleteUserByIdView:

    def __init__(self, repository: BaseUserRepository):
        self.__repository = repository

    async def delete_user_by_id(
        self,
        user_id: int,
    ):
        return await self.__repository.remove(user_id)
