from fastapi import FastAPI

from src.main.shared.amqp.amqp_consumer import AmqpConsumer
from src.main.shared.amqp.amqp_publisher import AmqpPublisher
from src.main.post.settings import settings
from src.main.post.util import handle_user_registration


class PostService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_registered_amqp_consumer = None
        self.initialize_amqp_consumers()

        self.post_created_amqp_publisher = None
        self.initialize_amqp_publishers()

    def initialize_amqp_consumers(self):
        self.user_registered_amqp_consumer = AmqpConsumer(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_USER_REGISTERED_EXCHANGE_NAME,
            incoming_message_handler=handle_user_registration,
        )

    def initialize_amqp_publishers(self):
        self.post_created_amqp_publisher = AmqpPublisher(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_POST_CREATED_EXCHANGE_NAME,
        )
