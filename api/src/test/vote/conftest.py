import pytest
from fastapi.testclient import TestClient

from src.main.vote.main import app
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

    def override_azure_scheme():
        return None

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]
