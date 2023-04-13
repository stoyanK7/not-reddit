from pydantic import BaseSettings

from src.main.env import get_env


class DatabaseSettings(BaseSettings):
    DB_DIALECT: str = get_env("DB_DIALECT")
    DB_USER: str = get_env("DB_USER")
    DB_PASSWORD: str = get_env("DB_PASSWORD")
    DB_NAME: str = get_env("DB_NAME")
    DB_HOST: str = get_env("DB_HOST")
    DB_PORT: str = get_env("DB_PORT")


settings = DatabaseSettings()
