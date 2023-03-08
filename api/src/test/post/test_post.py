from fastapi.testclient import TestClient
from fastapi import status

from src.main.post.main import app

client = TestClient(app)


def test_get_posts():
    """Test get posts."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "All posts"}


def test_create_post():
    """Test create post."""
    response = client.post("/", json={"title": "Test post"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'id': 1, 'title': 'Test post'}
