from fastapi import FastAPI

from src.main.shared.cors.cors import configure_cors
from src.main.shared.amqp.amqp_publisher import AmqpPublisher
from src.main.user.settings import settings


class UserService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        configure_cors(self)

        self.user_registered_amqp_publisher = None
        self.initialize_amqp_publishers()

    def initialize_amqp_publishers(self):
        self.user_registered_amqp_publisher = AmqpPublisher(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_USER_REGISTERED_EXCHANGE_NAME,
        )
