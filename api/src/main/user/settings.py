from src.main.settings import DatabaseSettings

from src.main.env import get_env


class UserServiceSettings(DatabaseSettings):
    RABBITMQ_HOST: str = get_env("RABBITMQ_HOST")
    RABBITMQ_EMAIL_QUEUE: str = get_env("RABBITMQ_EMAIL_QUEUE")


settings = UserServiceSettings()
