import pytest
from alembic.config import main as alembic
from starlette.config import environ
from starlette.testclient import TestClient

# putting the app in testing mode, informs config.py to use a separate test database
environ["TESTING"] = "TRUE"


@pytest.fixture
def client():
    from src.rando_server import load_app

    # migrate database to head (latest revision)
    alembic(["--raiseerr", "upgrade", "head"])

    # yield client until we're done with it
    with TestClient(load_app()) as client:
        yield client

    # then downgrade database to base (zero revisions)
    alembic(["--raiseerr", "downgrade", "base"])
