from repository.base import BaseUserRepository


class GetUserByIdView:

    def __init__(self, repository: BaseUserRepository):
        self.__repository = repository

    async def get_user_by_id(
        self,
        user_id: int,
    ):
        return await self.__repository.get(user_id)
