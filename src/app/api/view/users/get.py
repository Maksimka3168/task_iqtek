from repository.base import BaseUserRepository


class GetUserByIdView:

    def __init__(self, repository_: BaseUserRepository):
        self.repository = repository_

    async def get_user_by_id(
        self,
        user_id: int,
    ):
        return await self.repository.get(user_id)
