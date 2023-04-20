from typing import Union
from pydantic import AnyHttpUrl, BaseSettings

from src.main.env import get_env


class Settings(BaseSettings):
    # Auth
    APP_CLIENT_ID = get_env("APP_CLIENT_ID")
    OPENAPI_CLIENT_ID = get_env("OPENAPI_CLIENT_ID")
    # CORS
    CORS_ORIGINS: list[Union[str, AnyHttpUrl]] = [
        'http://localhost:8000',
        "http://localhost:8080",
        "http://localhost:3000",
    ]


settings = Settings()
