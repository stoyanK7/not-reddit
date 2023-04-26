import asyncio
from functools import partial

import aio_pika
import pika
from aio_pika import connect_robust
from aio_pika.abc import AbstractIncomingMessage, ExchangeType
from fastapi import FastAPI
from pika import BlockingConnection, ConnectionParameters

from src.main.post.util import insert_user_to_db
from src.main.user.settings import settings
from src.main.logger import logger


__all__ = [
    'consume'
]


async def on_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        print(f"[x] {message.body!r}")


async def consume(loop):
    connection = await connect_robust('amqp://guest:guest@localhost/', loop=loop)
    logger.info("Connected to RabbitMQ.")

    async with connection:
        # Creating a channel
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        logs_exchange = await channel.declare_exchange(
            "logs", ExchangeType.FANOUT,
        )

        # Declaring queue
        queue = await channel.declare_queue(exclusive=True)

        # Binding the queue to the exchange
        await queue.bind(logs_exchange)

        # Start listening the queue
        await queue.consume(on_message)

        logger.info(" [*] Waiting for logs. To exit press CTRL+C")
        await asyncio.Future()
