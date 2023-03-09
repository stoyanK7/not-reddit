"""This module is used for database connection and session management."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.event import listens_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
from src.main.database import Base, get_db
from src.main.post.main import app

database_url = "sqlite:///:memory:"
engine = create_engine(database_url,
                       connect_args={"check_same_thread": False},
                       poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Set up the database once
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


@listens_for(engine, "connect")
def do_connect(dbapi_connection, connection_record):
    """
    Disable pysqlite's emitting of the BEGIN statement entirely.
    Also stops it from emitting COMMIT before any DDL.
    """
    dbapi_connection.isolation_level = None


@listens_for(engine, "begin")
def do_begin(conn):
    """
    Emits our own BEGIN.
    """
    conn.exec_driver_sql("BEGIN")


@pytest.fixture
def session():
    """
    It creates a nested transaction, recreates it when the application code
    calls session.commit and rolls it back at the end.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    # Begin a nested transaction (using SAVEPOINT).
    nested = connection.begin_nested()

    # If the application code calls session.commit, it will end the nested
    # transaction. Need to start a new one when that happens.
    @listens_for(session, "after_transaction_end")
    def end_savepoint(session, transaction):
        nonlocal nested
        if not nested.is_active:
            nested = connection.begin_nested()

    yield session

    # Rollback the overall transaction, restoring the state before the test ran.
    session.close()
    transaction.rollback()
    connection.close()


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
