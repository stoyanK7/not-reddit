from src.main.shared.amqp.settings import AmqpSettings


class CommentServiceSettings(AmqpSettings):
    SERVICE_PREFIX: str = "/api/comment"
    AMQP_USER_REGISTERED_QUEUE_NAME: str = "comment_service_user_registered_queue"
    AMQP_POST_CREATED_QUEUE_NAME: str = "comment_service_post_created_queue"
    AMQP_COMMENT_VOTE_CASTED_QUEUE_NAME: str = "comment_service_comment_vote_casted_queue"
    AMQP_USER_DELETED_QUEUE_NAME: str = "comment_service_user_deleted_queue"


settings = CommentServiceSettings()
