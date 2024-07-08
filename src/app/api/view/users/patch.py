from api.users.schemas import UserPatch
from repository.base import BaseUserRepository
from models.user import User


class PatchEditUserByIdView:

    def __init__(self, repository_: BaseUserRepository):
        self.repository = repository_

    async def edit_user_by_id(
        self,
        user_patch: UserPatch,
    ):
        user = User(full_name=user_patch.full_name)
        user.id = user_patch.user_id
        return await self.repository.update(user)
