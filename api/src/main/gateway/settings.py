from pydantic import BaseSettings

from src.main.env import get_env


class Settings(BaseSettings):
    DB_DIALECT = get_env("DB_DIALECT")
    DB_USER = get_env("DB_USER")
    DB_PASSWORD = get_env("DB_PASSWORD")
    DB_NAME = get_env("DB_NAME")
    DB_HOST = get_env("DB_HOST")
    DB_PORT = get_env("DB_PORT")

    COMMENT_SERVICE_URL = get_env("COMMENT_SERVICE_URL")
    POST_SERVICE_URL = get_env("POST_SERVICE_URL")
    SUBREDDIT_SERVICE_URL = get_env("SUBREDDIT_SERVICE_URL")
    USER_SERVICE_URL = get_env("USER_SERVICE_URL")
    VOTE_SERVICE_URL = get_env("VOTE_SERVICE_URL")


settings = Settings()
