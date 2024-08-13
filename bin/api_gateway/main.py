import uvicorn

from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.gateway.users.users import users_router, init_users_endpoints
from app.bootstrap.initialization_app import initialize_app

load_dotenv()

app = FastAPI()


@app.on_event("startup")
async def startup():
    initialize_app(config_path="../../config.yml")
    init_users_endpoints()
    app.include_router(users_router)


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
