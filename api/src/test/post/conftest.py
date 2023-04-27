import pytest
from fastapi.testclient import TestClient

from src.main.post.model import Post as PostModel
from src.main.post.main import app
from src.main.shared.database.main import get_db, Base
from src.test.shared.database.main import engine

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
def insert_mock_text_posts():
    """Insert mock posts into the database."""

    def _insert_mock_posts(amount, session) -> list[PostModel]:
        posts: list[PostModel] = []
        for x in range(0, amount):
            post = {
                "title": f"Test post {x}",
                "body": f"Test body {x}"
            }
            model = PostModel(**post)
            posts.append(model)
            session.add(model)
        session.commit()
        return posts

    yield _insert_mock_posts
