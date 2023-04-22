from azure.communication.email import EmailClient

from src.main.email.settings import settings
from src.main.email.util import decode_and_convert_to_dict, construct_message
from src.main.logger import logger

email_client = EmailClient.from_connection_string(settings.EMAIL_CONNECTION_STRING)


def send_email(ch, method, properties, body):
    body = decode_and_convert_to_dict(body)
    recipients = body['recipients']
    content_topic = body['content_topic']

    try:
        message = construct_message(recipients=recipients, content_topic=content_topic)
        poller = email_client.begin_send(message)
        time_elapsed = 0

        while not poller.done():
            logger.info(f"Email send poller status: {poller.status()}")

            poller.wait(settings.POLLER_WAIT_TIME)
            time_elapsed += settings.POLLER_WAIT_TIME

            if time_elapsed > 18 * settings.POLLER_WAIT_TIME:
                raise RuntimeError("Polling timed out.")

        if poller.result()["status"] == "Succeeded":
            logger.info(f"Successfully sent email (operation id: {poller.result()['id']})")
        else:
            raise RuntimeError(str(poller.result()["error"]))
        logger.info("Result: ")
        logger.info(poller.result())
    except Exception as ex:
        logger.error('Exception:')
        logger.error(ex)