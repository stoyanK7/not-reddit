from typing import Union
from pydantic import AnyHttpUrl

from src.main.settings import DatabaseSettings
from src.main.env import get_env


class Settings(DatabaseSettings):
    # Paths
    COMMENT_SERVICE_URL = get_env("COMMENT_SERVICE_URL")
    POST_SERVICE_URL = get_env("POST_SERVICE_URL")
    SUBREDDIT_SERVICE_URL = get_env("SUBREDDIT_SERVICE_URL")
    USER_SERVICE_URL = get_env("USER_SERVICE_URL")
    VOTE_SERVICE_URL = get_env("VOTE_SERVICE_URL")
    # Auth
    APP_CLIENT_ID = get_env("APP_CLIENT_ID")
    OPENAPI_CLIENT_ID = get_env("OPENAPI_CLIENT_ID")
    SECRET_KEY = get_env("SECRET_KEY")
    # CORS
    CORS_ORIGINS: list[Union[str, AnyHttpUrl]] = ['http://localhost:8000']


settings = Settings()
