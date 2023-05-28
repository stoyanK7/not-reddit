from aio_pika import connect_robust, Message
from aio_pika.abc import ExchangeType, DeliveryMode
from aio_pika.exceptions import AMQPConnectionError

from src.main.shared.logger import logger


class AmqpPublisher:

    def __init__(self, amqp_url, exchange_name):
        self.amqp_url = amqp_url
        self.exchange_name = exchange_name
        self.exchange = None

    async def prepare_connection(self, loop):
        connection = await connect_robust(self.amqp_url, loop=loop)
        logger.info("Connected via AMQP.")

        channel = await connection.channel()
        logger.info("Channel opened.")

        prefetch_count = 1
        await channel.set_qos(prefetch_count=prefetch_count)

        exchange_type = ExchangeType.FANOUT
        self.exchange = await channel.declare_exchange(self.exchange_name, exchange_type)
        logger.info(f"Declared exchange '{self.exchange_name}' of type {exchange_type}.")

        return connection

    async def send_message(self, body: str):
        if not self.exchange:
            return
        message = Message(
            str.encode(body),
            delivery_mode=DeliveryMode.PERSISTENT,
        )
        await self.exchange.publish(message, routing_key=self.exchange_name)
