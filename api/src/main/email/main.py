import os
import sys

import pika

from src.main.email.send_email import send_email
from src.main.email.settings import settings
from src.main.logger import logger


def main():
    logger.info("Connecting to RabbitMQ.")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST))
    channel = connection.channel()

    queue_name = "email"
    logger.info(f"Declaring queue {queue_name}.")
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=send_email)
    logger.info("Waiting for messages. To exit press CTRL+C.")
    channel.start_consuming()


# PYTHONPATH=$(pwd) python3 src/main/email/main.py
try:
    main()
except KeyboardInterrupt:
    logger.info("Interrupted.")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
