from src.main.env import get_env


class PostServiceSettings:
    SERVICE_PREFIX: str = "/api/post"
    AMQP_URL: str = get_env("AMQP_URL")


settings = PostServiceSettings()
