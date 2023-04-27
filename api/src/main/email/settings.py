from pydantic import BaseSettings

from src.main.shared.env import get_env


class EmailSettings(BaseSettings):
    AMQP_URL = get_env("AMQP_URL")
    EMAIL_SENDER_ADDRESS: str = get_env("EMAIL_SENDER_ADDRESS")
    EMAIL_CONNECTION_STRING: str = get_env("EMAIL_CONNECTION_STRING")
    POLLER_WAIT_TIME: int = 10


settings = EmailSettings()
