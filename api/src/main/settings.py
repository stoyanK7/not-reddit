from pydantic import BaseSettings

from src.main.env import get_env


class DatabaseSettings(BaseSettings):
    DB_DIALECT = get_env("DB_DIALECT")
    DB_USER = get_env("DB_USER")
    DB_PASSWORD = get_env("DB_PASSWORD")
    DB_NAME = get_env("DB_NAME")
    DB_HOST = get_env("DB_HOST")
    DB_PORT = get_env("DB_PORT")


settings = DatabaseSettings()
