from aio_pika.abc import AbstractIncomingMessage

from src.main.comment import crud
from src.main.shared.amqp.amqp_util import decode_body_and_convert_to_dict
from src.main.shared.database.main import get_db


def handle_successful_registration(message: AbstractIncomingMessage) -> None:
    body = decode_body_and_convert_to_dict(message.body)
    username = body['username']
    oid = body['oid']
    db = next(get_db())
    crud.insert_user(db=db, username=username, oid=oid)
