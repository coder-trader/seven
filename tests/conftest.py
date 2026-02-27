import os

import pytest
from dotenv import load_dotenv

from deribit_auth import DeribitAuth


@pytest.fixture
def access_token():
    load_dotenv()
    key = os.getenv("KEY")
    if not key:
        raise ValueError("Client ID must be set in environment variables.")
    secret = os.getenv("SECRET")
    if not secret:
        raise ValueError("Client Secret must be set in environment variables.")
    auth = DeribitAuth(
        client_id=key,
        client_secret=secret,
    )
    return auth.get_token()
