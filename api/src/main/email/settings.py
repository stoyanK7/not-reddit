from pydantic import BaseSettings

from src.main.shared.amqp.settings import AmqpSettings
from src.main.shared.env import get_env


class EmailSettings(AmqpSettings):
    EMAIL_SENDER_ADDRESS: str = get_env("EMAIL_SENDER_ADDRESS")
    EMAIL_CONNECTION_STRING: str = get_env("EMAIL_CONNECTION_STRING")
    POLLER_WAIT_TIME: int = 10


settings = EmailSettings()
