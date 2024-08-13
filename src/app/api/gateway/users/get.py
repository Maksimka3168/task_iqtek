from app.services.users import UserService


class GetUserByIdView:

    def __init__(self, service: UserService):
        self.__service = service

    async def get_user_by_id(
        self,
        user_id: int,
    ):
        return await self.__service.get(user_id)
