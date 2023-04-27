from src.main.settings import AmqpSettings


class PostServiceSettings(AmqpSettings):
    SERVICE_PREFIX: str = "/api/post"


settings = PostServiceSettings()
