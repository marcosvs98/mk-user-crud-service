from decouple import config

ENV_SERVER = config("ENV_SERVER", default="LOCAL")
APPLICATION_NAME = config("APPLICATION_NAME")
PORT = config("PORT", default=8000, cast=int)
UVICORN_WORKERS = config("UVICORN_WORKERS", default=3, cast=int)

REDIS_HOST = config("REDIS_HOST", default="redis")
REDIS_PORT = config("REDIS_PORT", default=6379, cast=int)
REDIS_PASSWORD = config("REDIS_PASSWORD", None)
REDIS_SSL = config("REDIS_SSL", default=False, cast=bool)
CACHE_SILENT_MODE = config("CACHE_SILENT_MODE", default=True, cast=bool)

USE_DATABASE = config("USE_DATABASE", default=False, cast=bool)
if USE_DATABASE:
    DATABASE_URL = (
        f"mysql+pymysql://{config('DB_USER')}:{config('DB_PASSWORD')}@"
        f"{config('DB_HOST')}/{config('DB_NAME')}"
    )
else:
    DATABASE_URL = "sqlite:///db.sqlite"

ACCEPT_PARALLEL_REQUESTS = config("ACCEPT_PARALLEL_REQUESTS", default=False, cast=bool)
