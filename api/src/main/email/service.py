from src.main.email.settings import settings
from src.main.email.send_email import send_email
from src.main.shared.amqp.amqp_consumer import AmqpConsumer


class EmailService:
    def __init__(self):
        self.user_registered_amqp_consumer = None
        self.initialize_amqp_consumers()

    def initialize_amqp_consumers(self):
        self.user_registered_amqp_consumer = AmqpConsumer(
            settings.AMQP_URL,
            exchange_name=settings.AMQP_USER_REGISTERED_EXCHANGE_NAME,
            queue_name=settings.AMQP_USER_REGISTERED_QUEUE_NAME,
            incoming_message_handler=send_email,
        )
