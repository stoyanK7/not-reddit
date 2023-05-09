from typing import Union
from pydantic import AnyHttpUrl, BaseSettings

from src.main.shared.env import get_env


class AuthSettings(BaseSettings):
    SERVICE_PREFIX: str = "/api/auth"
    # Auth
    APP_CLIENT_ID = get_env("APP_CLIENT_ID")
    # CORS
    CORS_ORIGINS: list[Union[str, AnyHttpUrl]] = [
        'http://localhost:8000',
        "http://localhost:8080",
        "http://localhost:3000",
    ]


settings = AuthSettings()
