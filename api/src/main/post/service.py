from fastapi import FastAPI

from src.main.amqp_consumer import AmqpConsumer
from src.main.post.settings import settings
from src.main.post.util import handle_successful_registration


class PostService(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.successful_registration_amqp_consumer = None
        self.initialize_amqp_consumers()

    def initialize_amqp_consumers(self):
        self.successful_registration_amqp_consumer = AmqpConsumer(
            settings.AMQP_URL,
            exchange_name=settings.SUCCESSFUL_REGISTRATION_EXCHANGE_NAME,
            incoming_message_handler=handle_successful_registration,
        )
