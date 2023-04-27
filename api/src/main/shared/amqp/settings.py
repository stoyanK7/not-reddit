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
    AMQP_SUCCESSFUL_REGISTRATION_EXCHANGE_NAME: str = get_env(
        "AMQP_SUCCESSFUL_REGISTRATION_EXCHANGE_NAME")
