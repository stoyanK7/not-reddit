import asyncio

from aio_pika import connect_robust
from aio_pika.abc import ExchangeType

from src.main.logger import logger
from src.main.post.settings import settings
from src.main.post.util import on_successful_registration

__all__ = [
    'consume_messages'
]


async def consume_messages(loop):
    connection = await connect_robust(settings.AMQP_URL, loop=loop)
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

        await queue.consume(on_successful_registration)
        logger.info(f"Consuming messages from queue '{queue.name}'.")

        await asyncio.Future()
