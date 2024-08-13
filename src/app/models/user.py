from dataclasses import dataclass, field


@dataclass
class UserPatch:
    id: int
    full_name: str


@dataclass
class User:
    id: int = field(init=False)
    full_name: str


@dataclass
class UserResponse(User):
    id: int
