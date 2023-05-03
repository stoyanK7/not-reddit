from src.main.shared.amqp.settings import AmqpSettings


class VoteServiceSettings(AmqpSettings):
    SERVICE_PREFIX: str = "/api/vote"


settings = VoteServiceSettings()
