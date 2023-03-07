"""Test posts API."""
from fastapi.testclient import TestClient
from fastapi import status

from .posts import app

client = TestClient(app)


def test_get_posts():
    """Test get posts."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "All posts"}
