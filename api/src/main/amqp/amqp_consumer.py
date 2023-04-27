from aio_pika import connect_robust
from aio_pika.abc import ExchangeType, AbstractIncomingMessage

from src.main.logger import logger


class AmqpConsumer:

    def __init__(self, amqp_url, exchange_name, incoming_message_handler):
        self.amqp_url = amqp_url
        self.exchange_name = exchange_name
        self.incoming_message_handler = incoming_message_handler

    async def consume(self, loop):
        connection = await connect_robust(self.amqp_url, loop=loop)
        logger.info("Connected via AMQP.")

        channel = await connection.channel()
        logger.info("Channel opened.")

        prefetch_count = 1
        await channel.set_qos(prefetch_count=prefetch_count)
        logger.info(f"QoS set to {prefetch_count}.")

        exchange_type = ExchangeType.FANOUT
        exchange = await channel.declare_exchange(self.exchange_name, exchange_type)
        logger.info(f"Declared exchange '{self.exchange_name}' of type {exchange_type}.")

        queue = await channel.declare_queue(exclusive=True)
        logger.info(f"Declared queue '{queue.name}'.")

        await queue.bind(exchange)
        logger.info(f"Bound queue '{queue.name}' to exchange '{self.exchange_name}'.")

        await queue.consume(self.process_incoming_message, no_ack=False)
        logger.info(f"Consuming messages from queue '{queue.name}'.")

        return connection

    async def process_incoming_message(self, message: AbstractIncomingMessage):
        # TODO: Remove in the future
        logger.info('Received message.')
        if message.body:
            self.incoming_message_handler(message)
            await message.ack()
