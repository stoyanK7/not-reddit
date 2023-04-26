from src.main.env import get_env


class UserServiceSettings:
    RABBITMQ_HOST: str = get_env("RABBITMQ_HOST")


settings = UserServiceSettings()
