from repository.base import BaseUserRepository


class DeleteUserByIdView:

    def __init__(self, repository_: BaseUserRepository):
        self.repository = repository_

    async def delete_user_by_id(
        self,
        user_id: int,
    ):
        return await self.repository.remove(user_id)
