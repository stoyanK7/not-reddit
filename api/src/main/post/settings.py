from src.main.shared.env import get_env
from src.main.shared.amqp.settings import AmqpSettings


class PostServiceSettings(AmqpSettings):
    SERVICE_PREFIX: str = "/api/post"
    BLOB_STORAGE_ACCOUNT_NAME: str = get_env("BLOB_STORAGE_ACCOUNT_NAME")
    BLOB_STORAGE_CONNECTION_STRING: str = get_env("BLOB_STORAGE_CONNECTION_STRING")
    BLOB_STORAGE_IMAGES_CONTAINER_NAME: str = get_env("BLOB_STORAGE_IMAGES_CONTAINER_NAME")
    BLOB_STORAGE_VIDEOS_CONTAINER_NAME: str = get_env("BLOB_STORAGE_VIDEOS_CONTAINER_NAME")
    ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png"]
    ALLOWED_VIDEO_TYPES = ["video/mp4", "video/mpeg", "video/webm"]
    ALLOWED_FILE_TYPES = ALLOWED_IMAGE_TYPES + ALLOWED_VIDEO_TYPES


settings = PostServiceSettings()
