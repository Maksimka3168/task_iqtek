from fastapi import APIRouter

from api.users.users import users_router

root_router = APIRouter()
root_router.include_router(
    users_router,
    prefix="/users",
)
