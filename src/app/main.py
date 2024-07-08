import uvicorn

from fastapi import FastAPI

from api.users.users import users_router, init_users_endpoints
from factories.config_factory import ConfigFactoryStorage, YmlConfigFactory

from factories.repository_factory import StorageRepositoryFactory, MemoryRepositoryFactory, PostgresRepositoryFactory
from repository.base import BaseUserRepository
from utils.core.ioc import ioc

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.on_event("startup")
async def startup():
    config_factory_storage = ConfigFactoryStorage()
    config_factory_storage.register_factory(YmlConfigFactory())
    config = config_factory_storage.get_instance("config.yml")

    repository_factory_storage = StorageRepositoryFactory()
    repository_factory_storage.register_factory(MemoryRepositoryFactory())
    repository_factory_storage.register_factory(PostgresRepositoryFactory())
    repository = repository_factory_storage.get_instance(config.repositories.selected_repository,
                                                         settings=config.repositories.memory)
    ioc.set(BaseUserRepository, repository)

    init_users_endpoints()
    app.include_router(users_router)


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
