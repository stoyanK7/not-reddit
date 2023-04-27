from pydantic import BaseSettings

from src.main.env import get_env


class DatabaseSettings(BaseSettings):
    DB_DIALECT: str = get_env("DB_DIALECT")
    DB_USER: str = get_env("DB_USER")
    DB_PASSWORD: str = get_env("DB_PASSWORD")
    DB_NAME: str = get_env("DB_NAME")
    DB_HOST: str = get_env("DB_HOST")
    DB_PORT: str = get_env("DB_PORT")


db_settings = DatabaseSettings()


class AmqpSettings(BaseSettings):
    # Connection
    AMQP_USER: str = get_env("AMQP_USER")
    AMQP_PASSWORD: str = get_env("AMQP_PASSWORD")
    AMQP_HOST: str = get_env("AMQP_HOST")
    AMQP_PORT: int = get_env("AMQP_PORT")
    AMQP_URL: str = f"amqp://{AMQP_USER}:{AMQP_PASSWORD}@{AMQP_HOST}:{AMQP_PORT}"

    # Exchanges
    AMQP_SUCCESSFUL_REGISTRATION_EXCHANGE_NAME: str = get_env(
        "AMQP_SUCCESSFUL_REGISTRATION_EXCHANGE_NAME")
