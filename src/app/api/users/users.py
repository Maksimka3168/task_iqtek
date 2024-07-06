from fastapi import APIRouter

from view.users.delete import DeleteUserByIdView
from view.users.get import GetUserByIdView
from view.users.patch import PatchEditUserByIdView
from view.users.post import PostAddUserView

users_router = APIRouter(tags=["users"])
users_router.add_api_route(
    "/{user_id}",
    GetUserByIdView().get_user_by_id,
    methods=["GET"]
)
users_router.add_api_route(
    "/",
    PostAddUserView().add_user,
    methods=["POST"]
)
users_router.add_api_route(
    "/",
    PatchEditUserByIdView().edit_user_by_id,
    methods=["PATCH"]
)
users_router.add_api_route(
    "/{user_id}",
    DeleteUserByIdView().delete_user_by_id,
    methods=["DELETE"]
)