from pydantic import BaseModel


class UserCreate(BaseModel):
    full_name: str


class UserPatch(BaseModel):
    user_id: int
    full_name: str
