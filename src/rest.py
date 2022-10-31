from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import ACCEPT_PARALLEL_REQUESTS, CACHE_SILENT_MODE
from adapters.middlewares_adapter import PreventDuplicatesMiddleware
from adapters.redis_adapter import RedisAdapter
from packages.users.controllers.users_controller import UsersController
from packages.users.repository.users_repository import UsersRepository
from packages.users.services.users_service import UsersService


def init_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    if not ACCEPT_PARALLEL_REQUESTS:
        app.add_middleware(
            PreventDuplicatesMiddleware,
            cache=RedisAdapter(silent_mode=CACHE_SILENT_MODE)
        )


def init_routes(app: FastAPI):
    @app.get('/', status_code=200)
    async def health_check():
        return {'status': 'ok'}

    app.include_router(
        UsersController(UsersService(repository=UsersRepository())).router,
        tags=["users"],
        prefix="/api/users"
    )
