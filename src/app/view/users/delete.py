from ioc import ioc


class DeleteUserByIdView:

    async def delete_user_by_id(
        self,
        user_id: int,
    ):
        repository = ioc.repository
        return await repository.remove(user_id)
