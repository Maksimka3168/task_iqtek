from fastapi import APIRouter

from app.api.gateway.users.delete import DeleteUserByIdView
from app.api.gateway.users.get import GetUserByIdView
from app.api.gateway.users.patch import PatchEditUserByIdView
from app.api.gateway.users.post import PostAddUserView
from app.repository.base import BaseUserRepository
from app.services.users import UserService
from app.utils.ioc import ioc

users_router = APIRouter(tags=["users"])


def init_users_endpoints():
    users_router.add_api_route(
        "/{user_id}",
        GetUserByIdView(
            service=UserService(
                repository=ioc.get(BaseUserRepository)
            )
        ).get_user_by_id,
        methods=["GET"]
    )
    users_router.add_api_route(
        "/",
        PostAddUserView(
            service=UserService(
                repository=ioc.get(BaseUserRepository)
            )
        ).add_user,
        methods=["POST"]
    )
    users_router.add_api_route(
        "/",
        PatchEditUserByIdView(
            service=UserService(
                repository=ioc.get(BaseUserRepository)
            )
        ).edit_user_by_id,
        methods=["PATCH"]
    )
    users_router.add_api_route(
        "/{user_id}",
        DeleteUserByIdView(
            service=UserService(
                repository=ioc.get(BaseUserRepository)
            )
        ).delete_user_by_id,
        methods=["DELETE"]
    )
