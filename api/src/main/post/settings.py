from src.main.env import get_env


class PostServiceSettings:
    AMQP_URL = get_env("AMQP_URL")


settings = PostServiceSettings()
