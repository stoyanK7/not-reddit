import os

from aio_pika.abc import AbstractIncomingMessage
from fastapi import UploadFile
from azure.storage.blob import BlobServiceClient

from src.main.post.storage import settings
from src.main.rabbitmq_util import decode_body_and_convert_to_dict

current_dir = os.getcwd()


async def upload_file(file: UploadFile):
    if settings.BLOB_STORAGE_CONNECTION_STRING:
        await upload_file_to_blob_storage(file)
    else:
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


async def on_successful_registration(message: AbstractIncomingMessage) -> None:
    async with message.process():
        body = decode_body_and_convert_to_dict(message.body)
        print(body)
