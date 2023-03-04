"""This is the main entrypoint for the API."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    This is the root endpoint.
    """
    return {"Hello": "World"}
