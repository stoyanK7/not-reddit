from fastapi import FastAPI

from src.main.shared.amqp.amqp_publisher import AmqpPublisher
from src.main.user.settings import settings


class UserService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_registration_amqp_publisher = None
        self.initialize_amqp_publishers()

    def initialize_amqp_publishers(self):
        self.user_registration_amqp_publisher = AmqpPublisher(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_USER_REGISTRATION_EXCHANGE_NAME,
        )
