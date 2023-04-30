import pytest
from fastapi.testclient import TestClient

from src.main.user.main import app
from src.main.user.model import User as UserModel
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
def mock_user():
    return {
        "email": "testemail",
    }


@pytest.fixture
def mock_user_with_username():
    return {
        "email": "testemail",
        "username": "testusername",
    }


@pytest.fixture
def insert_user():
    """Insert a user into the database."""

    def _insert_user(user, session) -> UserModel:
        model = UserModel(**user)
        session.add(model)
        session.commit()
        return model

    yield _insert_user
