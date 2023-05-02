from fastapi import FastAPI

from src.main.shared.amqp.amqp_consumer import AmqpConsumer
from src.main.comment.settings import settings
from src.main.comment.util import handle_user_registration


class CommentService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_registration_amqp_consumer = None
        # TODO: create vote consumer
        self.initialize_amqp_consumers()

    def initialize_amqp_consumers(self):
        self.user_registration_amqp_consumer = AmqpConsumer(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_USER_REGISTRATION_EXCHANGE_NAME,
            incoming_message_handler=handle_user_registration,
        )
