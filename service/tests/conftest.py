import pytest

from main import create_app


@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()
