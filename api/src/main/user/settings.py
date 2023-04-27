from src.main.amqp.settings import AmqpSettings


class UserServiceSettings(AmqpSettings):
    SERVICE_PREFIX: str = "/api/user"


settings = UserServiceSettings()
