from app.services.users import UserService


class DeleteUserByIdView:

    def __init__(self, service: UserService):
        self.__service = service

    async def delete_user_by_id(
        self,
        user_id: int,
    ):
        return await self.__service.remove(user_id)
