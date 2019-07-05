import os

from brivo import Brivo

USERNAME = os.environ["BRIVO_SANDBOX_USERNAME"]
PASSWORD = os.environ["BRIVO_SANDBOX_PASSWORD"]
CLIENT_ID = os.environ["BRIVO_SANDBOX_CLIENT_ID"]
CLIENT_SECRET = os.environ["BRIVO_SANDBOX_CLIENT_SECRET"]
API_KEY = os.environ["BRIVO_API_KEY"]


def test_token():
    brivo = Brivo(username=USERNAME, password=PASSWORD, client_id=CLIENT_ID,
                  client_secret=CLIENT_SECRET, api_key=API_KEY)
    # Make sure we can get reasonable data out of the token
    assert int(brivo._token["expires_at"]) > 1562288222


def test_users():
    brivo = Brivo(username=USERNAME, password=PASSWORD, client_id=CLIENT_ID,
                  client_secret=CLIENT_SECRET, api_key=API_KEY)
    users = brivo.users
    # I created users in the sandbox with last names of "Example" and "Test"
    assert [u["lastName"] for u in users] == ["Example", "Test"]
