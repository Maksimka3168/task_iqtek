from app.api.gateway.users.schemas import UserPatch
from app.models.user import User
from app.services.users import UserService


class PatchEditUserByIdView:

    def __init__(self, service: UserService):
        self.__service = service

    async def edit_user_by_id(
        self,
        user_patch: UserPatch,
    ):
        user = User(full_name=user_patch.full_name)
        user.id = user_patch.user_id
        return await self.__service.update(user)
