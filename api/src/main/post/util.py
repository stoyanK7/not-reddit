import json
import os

from aio_pika.abc import AbstractIncomingMessage
from fastapi import UploadFile, Request, HTTPException
from fastapi.responses import FileResponse
from azure.storage.blob import BlobServiceClient
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from src.main.shared.database.main import get_db
from src.main.post import crud
from src.main.post.settings import settings
from src.main.post.model import Post as PostModel
from src.main.shared.amqp.amqp_util import decode_body_and_convert_to_dict
from src.main.shared.jwt_util import get_access_token_oid

current_file = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file)
files_directory = f"{parent_directory}/files"


async def upload_file(file: UploadFile, post_id: int):
    # TODO: Remove back to normal
    # if settings.BLOB_STORAGE_CONNECTION_STRING:
    #     await upload_file_to_blob_storage(file)
    # else:
    await upload_file_to_local_storage(file)


def rename_file(file: UploadFile, post_id: int) -> UploadFile:
    """Rename file to postId.fileType"""
    file.filename = f"{post_id}.{file.filename.split('.')[-1]}"
    return file


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
    file_location = f"{files_directory}/{file.filename}"

    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())


def delete_file_from_post(post: PostModel):
    # if settings.BLOB_STORAGE_CONNECTION_STRING:
    #     delete_file_from_blob_storage(post=post)
    # else:
    delete_file_from_local_storage(post=post)


def delete_file_from_local_storage(post: PostModel):
    file_location = f"{files_directory}/{post.body.split('/')[-1]}"
    if os.path.exists(file_location):
        os.remove(file_location)


def handle_user_registration(message: AbstractIncomingMessage) -> None:
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


def assert_file_type_is_allowed(file: UploadFile):
    if file.content_type not in settings.ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="File type not allowed"
        )


def determine_storage_container_name(file: UploadFile) -> str:
    if file.content_type in settings.ALLOWED_IMAGE_TYPES:
        return settings.BLOB_STORAGE_IMAGES_CONTAINER_NAME
    elif file.content_type in settings.ALLOWED_VIDEO_TYPES:
        return settings.BLOB_STORAGE_VIDEOS_CONTAINER_NAME


def construct_file_response(name: str) -> FileResponse:
    file_location = f"{files_directory}/{name}"
    if os.path.exists(file_location):
        return FileResponse(file_location)
    else:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="File not found"
        )


async def emit_post_creation_event(request: Request, post: dict):
    body = json.dumps(post)
    await request.app.post_created_amqp_publisher.send_message(str(body))


def handle_vote_casted(message: AbstractIncomingMessage) -> None:
    body = decode_body_and_convert_to_dict(message.body)
    db = next(get_db())
    if body["vote_type"] == "up":
        crud.cast_upvote(db=db, post_id=body["post_id"])
    elif body["vote_type"] == "down":
        crud.cast_downvote(db=db, post_id=body["post_id"])


def handle_user_deleted(message: AbstractIncomingMessage) -> None:
    body = decode_body_and_convert_to_dict(message.body)
    db = next(get_db())
    crud.delete_user(db=db, oid=body["oid"])
    username = crud.get_username_by_oid(db=db, oid=body["oid"])
    crud.delete_user_posts(db=db, username=username)
