from fastapi import FastAPI

from src.main.shared.amqp.amqp_consumer import AmqpConsumer
from src.main.vote.settings import settings
from src.main.vote.util import handle_user_registration, handle_post_creation, \
    handle_comment_creation


class VoteService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_registration_amqp_consumer = None
        self.post_creation_amqp_consumer = None
        self.comment_creation_amqp_consumer = None

        self.initialize_amqp_consumers()

    def initialize_amqp_consumers(self):
        self.user_registration_amqp_consumer = AmqpConsumer(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_USER_REGISTERED_EXCHANGE_NAME,
            incoming_message_handler=handle_user_registration
        )
        self.post_creation_amqp_consumer = AmqpConsumer(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_POST_CREATED_EXCHANGE_NAME,
            incoming_message_handler=handle_post_creation
        )
        self.comment_creation_amqp_consumer = AmqpConsumer(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_COMMENT_CREATION_EXCHANGE_NAME,
            incoming_message_handler=handle_comment_creation
        )
