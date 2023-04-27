from src.main.env import get_env
from src.main.amqp.settings import AmqpSettings


class PostServiceSettings(AmqpSettings):
    SERVICE_PREFIX: str = "/api/post"
    BLOB_STORAGE_CONNECTION_STRING: str = get_env("BLOB_STORAGE_CONNECTION_STRING")
    BLOB_STORAGE_IMAGES_CONTAINER_NAME: str = get_env("BLOB_STORAGE_IMAGES_CONTAINER_NAME")
    BLOB_STORAGE_VIDEOS_CONTAINER_NAME: str = get_env("BLOB_STORAGE_VIDEOS_CONTAINER_NAME")


settings = PostServiceSettings()
