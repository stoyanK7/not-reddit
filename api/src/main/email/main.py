import asyncio
import os
import sys

from aio_pika import connect_robust
from aio_pika.abc import ExchangeType

from src.main.email.send_email import send_email
from src.main.email.settings import settings
from src.main.logger import logger


async def consume_messages():
    connection = await connect_robust(settings.AMQP_URL)
    logger.info("Connected via AMQP.")

    async with connection:
        channel = await connection.channel()
        logger.info("Channel opened.")

        prefetch_count = 1
        await channel.set_qos(prefetch_count=prefetch_count)
        logger.info(f"QoS set to {prefetch_count}.")

        exchange_name = "successful_registration"
        exchange_type = ExchangeType.FANOUT
        exchange = await channel.declare_exchange(exchange_name, exchange_type)
        logger.info(f"Declared exchange '{exchange_name}' of type {exchange_type}.")

        queue = await channel.declare_queue(exclusive=True)
        logger.info(f"Declared queue '{queue.name}'.")

        await queue.bind(exchange)
        logger.info(f"Bound queue '{queue.name}' to exchange '{exchange_name}'.")

        await queue.consume(send_email)
        logger.info(f"Consuming messages from queue '{queue.name}'.")

        await asyncio.Future()


try:
    asyncio.run(consume_messages())
except KeyboardInterrupt:
    logger.info("Interrupted.")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
