import uvicorn

from fastapi import FastAPI

from api.users.users import users_router
from factories.config_factory import ConfigFactoryStorage, YmlConfigFactory

from factories.repository_factory import RepositoryFactoryStorage, RepositoryMemoryFactory, RepositoryPostgresFactory
from utils.core.ioc import ioc

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.on_event("startup")
async def startup():
    config_factory_storage = ConfigFactoryStorage()
    await config_factory_storage.register_factory(YmlConfigFactory())
    config = await config_factory_storage.get_instance("yml")

    repository_factory_storage = RepositoryFactoryStorage()
    await repository_factory_storage.register_factory(RepositoryMemoryFactory())
    await repository_factory_storage.register_factory(RepositoryPostgresFactory())
    repository = await repository_factory_storage.get_instance(config["repositories"]["selected_repository"],
                                                               settings=config["repositories"][config["repositories"]
                                                               ["selected_repository"]])
    ioc.repository = repository


app.include_router(users_router)


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
