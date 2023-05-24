from src.main.shared.amqp.settings import AmqpSettings


class VoteServiceSettings(AmqpSettings):
    SERVICE_PREFIX: str = "/api/vote"
    AMQP_USER_REGISTERED_QUEUE_NAME: str = "vote_service_user_registered_queue"
    AMQP_POST_CREATED_QUEUE_NAME: str = "vote_service_post_created_queue"
    AMQP_COMMENT_CREATED_QUEUE_NAME: str = "vote_service_comment_created_queue"
    AMQP_USER_DELETED_QUEUE_NAME: str = "vote_service_user_deleted_queue"


settings = VoteServiceSettings()
