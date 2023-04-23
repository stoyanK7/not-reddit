from src.main.env import get_env


class UserServiceSettings:
    RABBITMQ_HOST: str = get_env("RABBITMQ_HOST")
    RABBITMQ_EMAIL_QUEUE: str = get_env("RABBITMQ_EMAIL_QUEUE")


settings = UserServiceSettings()
