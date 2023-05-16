import json

from pydantic import BaseSettings

from src.main.shared.env import get_env


class CorsSettings(BaseSettings):
    CORS_ALLOWED_ORIGINS: list[str] = json.loads(get_env("CORS_ALLOWED_ORIGINS", '["*"]'))


settings = CorsSettings()
