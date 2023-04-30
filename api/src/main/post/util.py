import os

from aio_pika.abc import AbstractIncomingMessage
from fastapi import UploadFile, Request, HTTPException
from azure.storage.blob import BlobServiceClient
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from src.main.shared.database.main import get_db
from src.main.post import crud
from src.main.post.settings import settings
from src.main.shared.amqp.amqp_util import decode_body_and_convert_to_dict
from src.main.shared.jwt_util import get_access_token_oid

current_dir = os.getcwd()


async def upload_file(file: UploadFile):
    # TODO: Remove back to normal
    # if settings.BLOB_STORAGE_CONNECTION_STRING:
    #     await upload_file_to_blob_storage(file)
    # else:
    await upload_file_to_local_storage(file)


async def upload_file_to_blob_storage(file: UploadFile):
    try:
        print("Azure Blob Storage Python quickstart sample")
        blob_service_client = BlobServiceClient.from_connection_string(
            settings.BLOB_STORAGE_CONNECTION_STRING
        )
        # file_type = file.content_type
        container_client = blob_service_client.get_container_client("images")
        blob_client = container_client.get_blob_client(file.filename)

        f = await file.read()
        await blob_client.upload_blob(f)

    except Exception as ex:
        print('Exception:')
        print(ex)


async def upload_file_to_local_storage(file: UploadFile):
    file_location = f"{current_dir}/src/main/post/files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())


def handle_successful_registration(message: AbstractIncomingMessage) -> None:
    body = decode_body_and_convert_to_dict(message.body)
    username = body['username']
    oid = body['oid']
    db = next(get_db())
    crud.insert_user(db=db, username=username, oid=oid)


def assert_user_is_owner_of_post(db: Session, request: Request, post_id: int):
    oid = get_access_token_oid(request=request)
    username = crud.get_username_by_oid(db=db, oid=oid)

    post = crud.get_post_by_id(db=db, post_id=post_id)
    if post.username != username:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="You are not the owner of this post"
        )


def get_username_from_access_token(db: Session, request: Request) -> str:
    oid = get_access_token_oid(request=request)
    return crud.get_username_by_oid(db=db, oid=oid)
