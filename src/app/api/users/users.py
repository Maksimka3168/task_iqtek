from fastapi import APIRouter

from api.view.users.delete import DeleteUserByIdView
from api.view.users.get import GetUserByIdView
from api.view.users.patch import PatchEditUserByIdView
from api.view.users.post import PostAddUserView
from repository.base import BaseUserRepository
from utils.core.ioc import ioc

users_router = APIRouter(tags=["users"])


def init_users_endpoints():
    users_router.add_api_route(
        "/{user_id}",
        GetUserByIdView(
            repository=ioc.get(BaseUserRepository)
        ).get_user_by_id,
        methods=["GET"]
    )
    users_router.add_api_route(
        "/",
        PostAddUserView(
            repository=ioc.get(BaseUserRepository)
        ).add_user,
        methods=["POST"]
    )
    users_router.add_api_route(
        "/",
        PatchEditUserByIdView(
            repository=ioc.get(BaseUserRepository)
        ).edit_user_by_id,
        methods=["PATCH"]
    )
    users_router.add_api_route(
        "/{user_id}",
        DeleteUserByIdView(
            repository=ioc.get(BaseUserRepository)
        ).delete_user_by_id,
        methods=["DELETE"]
    )
