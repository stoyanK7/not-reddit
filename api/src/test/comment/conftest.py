import pytest
from fastapi.testclient import TestClient

from src.main.comment.main import app
from src.main.comment.model import Comment as CommentModel
from src.main.database import get_db, Base
from src.test.database import engine

# Set up the database once.
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


@pytest.fixture
def client(session):
    """
    A fixture for the fastapi test client which depends on the
    previous session fixture. Instead of creating a new session in the
    dependency override as before, it uses the one provided by the
    session fixture.
    """

    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]


@pytest.fixture
def insert_mock_comments():
    """Insert mock comments into the database."""

    def _insert_mock_comments(amount, session) -> list[CommentModel]:
        comments: list[CommentModel] = []
        for x in range(0, amount):
            comment = {
                "body": f"Test comment {x}",
                "user_id": x,
                "post_id": x,
            }
            model = CommentModel(**comment)
            comments.append(model)
            session.add(model)
        session.commit()
        return comments

    yield _insert_mock_comments
