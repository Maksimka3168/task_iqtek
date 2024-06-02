from typing import Annotated

from fastapi import APIRouter, Depends

from application.models.user import User
from repository.base import BaseUserRepository

from api.users.schemas import UserCreate, UserPatch

users_router = APIRouter()


@users_router.get("/{user_id}")
async def get_user_by_id(
    user_id: int,
    repository: Annotated[BaseUserRepository, Depends()]
):
    return await repository.get(user_id)


@users_router.post("/")
async def add_user(
    user_create: UserCreate,
    repository: Annotated[BaseUserRepository, Depends()]
):
    user_info = await repository.add(User(
        full_name=user_create.full_name
    ))
    return user_info


@users_router.patch("/")
async def edit_user_by_id(
    user_patch: UserPatch,
    repository: Annotated[BaseUserRepository, Depends()]
):
    user = User(full_name=user_patch.full_name)
    user.id = user_patch.user_id
    return await repository.update(user)


@users_router.delete("/{user_id}")
async def delete_user_by_id(
    user_id: int,
    repository: Annotated[BaseUserRepository, Depends()]
):
    return await repository.remove(user_id)
