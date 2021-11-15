import pytest
from mongoengine import connect, disconnect
from starlette.testclient import TestClient

from api.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture()
def mongo(scope='function'):
    # disconnect the default connection
    disconnect('default')
    # it is going to create a new connection and record to db
    db = connect('test_db', host='mongodb://localhost')
    # this parameter yield is going to provide the db parameter and when the function finished it
    # it is going to return here to drop de bank.
    yield db
    db.drop_database('test_db')
    disconnect('default')
