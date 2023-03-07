"""Posts API."""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_posts():
    """Get all posts."""
    return {"message": "All posts"}
