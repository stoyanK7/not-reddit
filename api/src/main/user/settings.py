from src.main.settings import AmqpSettings


class UserServiceSettings(AmqpSettings):
    SERVICE_PREFIX: str = "/api/user"


settings = UserServiceSettings()
