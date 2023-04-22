from pydantic import BaseSettings

from src.main.env import get_env


class EmailSettings(BaseSettings):
    RABBITMQ_HOST: str = get_env("RABBITMQ_HOST")
    EMAIL_SENDER_ADDRESS: str = get_env("EMAIL_SENDER_ADDRESS")
    EMAIL_CONNECTION_STRING: str = get_env("EMAIL_CONNECTION_STRING")
    POLLER_WAIT_TIME: int = 10


settings = EmailSettings()