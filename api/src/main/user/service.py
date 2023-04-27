from fastapi import FastAPI

from src.main.amqp.amqp_publisher import AmqpPublisher
from src.main.user.settings import settings


class UserService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.successful_registration_amqp_publisher = None
        self.initialize_amqp_publishers()

    def initialize_amqp_publishers(self):
        self.successful_registration_amqp_publisher = AmqpPublisher(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_SUCCESSFUL_REGISTRATION_EXCHANGE_NAME,
        )
