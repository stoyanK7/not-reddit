from src.main.shared.amqp.settings import AmqpSettings
from src.main.shared.env import get_env


class EmailSettings(AmqpSettings):
    AMQP_USER_REGISTERED_QUEUE_NAME: str = "email_service_user_registered_queue"
    EMAIL_SENDER_ADDRESS: str = get_env("EMAIL_SENDER_ADDRESS")
    EMAIL_CONNECTION_STRING: str = get_env("EMAIL_CONNECTION_STRING")
    POLLER_WAIT_TIME: int = 10


settings = EmailSettings()
