import uvicorn

from fastapi import FastAPI, Depends

from api.root import root_router
from factorys.repository_factory import RepositoryFactoryStorage, RepositoryMemoryFactory, RepositoryPostgresFactory
from ioc import ioc

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(root_router)


@app.on_event("startup")
async def startup():
    repository_factory_storage = RepositoryFactoryStorage()
    await repository_factory_storage.register_factory(RepositoryMemoryFactory)
    await repository_factory_storage.register_factory(RepositoryPostgresFactory)
    repository = await repository_factory_storage.get_instance("postgres", settings=...)
    ioc.repository = repository


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
