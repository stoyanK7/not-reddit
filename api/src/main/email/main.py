import asyncio
import os
import sys

from src.main.email.service import EmailService
from src.main.shared.logger import logger

app = EmailService()

try:
    loop = asyncio.get_event_loop()
    connection = loop.run_until_complete(app.successful_registration_amqp_consumer.consume(loop))
    loop.run_forever()
    loop.run_until_complete(connection.close())
except KeyboardInterrupt:
    logger.info("Interrupted.")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
