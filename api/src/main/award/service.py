from fastapi import FastAPI

from main.award.settings import settings
from main.shared.amqp.amqp_publisher import AmqpPublisher


class AwardService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.post_awarded_amqp_publisher = None
        self.comment_awarded_amqp_publisher = None
        self.initialize_amqp_publishers()

    def initialize_amqp_publishers(self):
        self.post_awarded_amqp_publisher = AmqpPublisher(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_POST_AWARDED_EXCHANGE_NAME
        )
        self.comment_awarded_amqp_publisher = AmqpPublisher(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_COMMENT_AWARDED_EXCHANGE_NAME
        )
