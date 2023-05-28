from aio_pika import connect_robust
from aio_pika.abc import ExchangeType, AbstractIncomingMessage
from aio_pika.exceptions import AMQPConnectionError

from src.main.shared.logger import logger


class AmqpConsumer:

    def __init__(self, amqp_url, exchange_name, queue_name, incoming_message_handler):
        self.amqp_url = amqp_url
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.incoming_message_handler = incoming_message_handler

    async def consume(self, loop):
        connection = await connect_robust(self.amqp_url, loop=loop)
        logger.info("Connected via AMQP.")

        channel = await connection.channel()
        logger.info("Channel opened.")

        prefetch_count = 1
        await channel.set_qos(prefetch_count=prefetch_count)

        exchange_type = ExchangeType.FANOUT
        exchange = await channel.declare_exchange(self.exchange_name, exchange_type)
        logger.info(f"Declared exchange '{self.exchange_name}' of type {exchange_type}.")

        queue = await channel.declare_queue(exclusive=False, name=self.queue_name)
        logger.info(f"Declared queue '{self.queue_name}'.")

        await queue.bind(exchange)
        logger.info(f"Bound queue '{self.queue_name}' to exchange '{self.exchange_name}'.")

        await queue.consume(self.process_incoming_message, no_ack=False)
        logger.info(f"Consuming messages from queue '{self.queue_name}'.")

        return connection

    async def process_incoming_message(self, message: AbstractIncomingMessage):
        if message.body:
            self.incoming_message_handler(message)
            await message.ack()
