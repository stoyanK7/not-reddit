from fastapi import FastAPI

from src.main.shared.amqp.amqp_consumer import AmqpConsumer
from src.main.comment.settings import settings
from src.main.comment.util import handle_user_registration, handle_post_creation
from src.main.shared.amqp.amqp_publisher import AmqpPublisher


class CommentService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_registered_amqp_consumer = None
        self.post_created_amqp_consumer = None
        # TODO: create vote consumer
        self.initialize_amqp_consumers()

        self.comment_created_amqp_publisher = None
        self.initialize_amqp_publishers()

    def initialize_amqp_consumers(self):
        # TODO: change name
        self.user_registered_amqp_consumer = AmqpConsumer(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_USER_REGISTERED_EXCHANGE_NAME,
            incoming_message_handler=handle_user_registration,
        )

        self.post_created_amqp_consumer = AmqpConsumer(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_POST_CREATED_EXCHANGE_NAME,
            incoming_message_handler=handle_post_creation,
        )

    def initialize_amqp_publishers(self):
        self.comment_created_amqp_publisher = AmqpPublisher(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_COMMENT_CREATED_EXCHANGE_NAME,
        )
