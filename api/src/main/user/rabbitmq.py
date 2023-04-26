from pika import BlockingConnection, ConnectionParameters

from src.main.user.settings import settings
from src.main.logger import logger

channel = None
rabbitmq_connection = None


def connect_to_rabbitmq():
    global rabbitmq_connection
    global channel

    rabbitmq_connection = BlockingConnection(ConnectionParameters(host=settings.RABBITMQ_HOST))
    channel = rabbitmq_connection.channel()
    logger.info("Connected to RabbitMQ.")

    channel.queue_declare(queue=settings.RABBITMQ_EMAIL_QUEUE)
    logger.info(f"Declared queue '{settings.RABBITMQ_EMAIL_QUEUE}'.")


def disconnect_from_rabbitmq():
    global rabbitmq_connection
    global channel

    channel.close()
    rabbitmq_connection.close()
    logger.info("Disconnected from RabbitMQ.")
