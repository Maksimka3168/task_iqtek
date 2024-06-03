import os
from functools import partial

import uvicorn
from fastapi import FastAPI, Depends

from adapters.sqlalchemy_db.session import get_async_session, create_session_maker
from api.root import root_router
from repository.base import BaseUserRepository
from repository.database import PostgresUserRepository
from repository.memory import MemoryUserRepository

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(root_router)


@app.on_event("startup")
async def startup():
    if os.getenv("REPOSITORY_TYPE") == "Memory":
        repository = MemoryUserRepository()
        get_repository = lambda: repository
    elif os.getenv("REPOSITORY_TYPE") == "Postgres":
        session_maker = await create_session_maker()
        get_repository = lambda x=Depends(partial(get_async_session, session_maker)): PostgresUserRepository(session=x)
    else:
        raise ValueError("Invalid repository type")

    app.dependency_overrides[BaseUserRepository] = get_repository


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
