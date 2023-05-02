from src.main.shared.amqp.settings import AmqpSettings


class CommentServiceSettings(AmqpSettings):
    SERVICE_PREFIX: str = "/api/comment"


settings = CommentServiceSettings()
