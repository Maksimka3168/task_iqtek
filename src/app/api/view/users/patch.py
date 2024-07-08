from api.users.schemas import UserPatch
from utils.core.ioc import ioc
from models.user import User


class PatchEditUserByIdView:

    async def edit_user_by_id(
        self,
        user_patch: UserPatch,
    ):
        repository = ioc.repository
        user = User(full_name=user_patch.full_name)
        user.id = user_patch.user_id
        return await repository.update(user)
