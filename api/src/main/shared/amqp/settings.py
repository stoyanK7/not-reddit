from pydantic import BaseSettings

from src.main.shared.env import get_env


class AmqpSettings(BaseSettings):
    # Connection
    AMQP_USER: str = get_env("AMQP_USER")
    AMQP_PASSWORD: str = get_env("AMQP_PASSWORD")
    AMQP_HOST: str = get_env("AMQP_HOST")
    AMQP_PORT: str = get_env("AMQP_PORT")
    AMQP_URL: str = f"amqp://{AMQP_USER}:{AMQP_PASSWORD}@{AMQP_HOST}:{AMQP_PORT}"

    # Exchanges
    AMQP_USER_REGISTERED_EXCHANGE_NAME: str = get_env("AMQP_USER_REGISTERED_EXCHANGE_NAME")
    AMQP_POST_CREATED_EXCHANGE_NAME: str = get_env("AMQP_POST_CREATED_EXCHANGE_NAME")
    AMQP_COMMENT_CREATED_EXCHANGE_NAME: str = get_env("AMQP_COMMENT_CREATED_EXCHANGE_NAME")
    AMQP_POST_VOTE_CASTED_EXCHANGE_NAME: str = get_env("AMQP_POST_VOTE_CASTED_EXCHANGE_NAME")
    AMQP_COMMENT_VOTE_CASTED_EXCHANGE_NAME: str = get_env("AMQP_COMMENT_VOTE_CASTED_EXCHANGE_NAME")
