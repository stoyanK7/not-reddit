"""This is the main entrypoint for the API."""

from fastapi import FastAPI
import pika

app = FastAPI()


@app.get("/")
def read_root():
    """
    This is the root endpoint.
    """
    return {"Hello": "World"}


@app.get("/send")
def send_message(body: str):
    """
    This is the send endpoint.
    """
    credentials = pika.PlainCredentials("root", "root")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost", credentials=credentials)
    )
    channel = connection.channel()
    queue = "hello"
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange="", routing_key=queue, body=body)
    connection.close()
    return {"message": body}
