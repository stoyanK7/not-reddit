from aio_pika.abc import AbstractIncomingMessage

from src.main.shared.logger import logger


def send_email(message: AbstractIncomingMessage) -> None:
    logger.info("Sending email...")
