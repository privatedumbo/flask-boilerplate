from app import create_app
from app.core.users import User
from app.core.status import ACTIVE, INACTIVE

import pytest


@pytest.fixture
def test_app():
    app = create_app()
    return app.test_client()


@pytest.fixture
def user_builder():

    def _user_builder(name: str, status: str = ACTIVE):
        user = User(name=name, status=status)
        return user

    return _user_builder
