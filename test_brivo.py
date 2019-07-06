import os

from brivo import Brivo

USERNAME = os.environ["BRIVO_SANDBOX_USERNAME"]
PASSWORD = os.environ["BRIVO_SANDBOX_PASSWORD"]
CLIENT_ID = os.environ["BRIVO_SANDBOX_CLIENT_ID"]
CLIENT_SECRET = os.environ["BRIVO_SANDBOX_CLIENT_SECRET"]
API_KEY = os.environ["BRIVO_API_KEY"]

# I created users in the brivo sandbox with these last names
EXAMPLE_LAST_NAME = "Example"
TEST_LAST_NAME = "Test"
USER_LAST_NAMES = [EXAMPLE_LAST_NAME, TEST_LAST_NAME]


def test_token():
    brivo = Brivo(username=USERNAME, password=PASSWORD, client_id=CLIENT_ID,
                  client_secret=CLIENT_SECRET, api_key=API_KEY)
    # Make sure we can get reasonable data out of the token
    assert int(brivo._token["expires_at"]) > 1562288222


def test_users():
    brivo = Brivo(username=USERNAME, password=PASSWORD, client_id=CLIENT_ID,
                  client_secret=CLIENT_SECRET, api_key=API_KEY)
    users = brivo.users()
    assert sorted([u["lastName"] for u in users]) == USER_LAST_NAMES


def test_users_with_optional_field():
    brivo = Brivo(username=USERNAME, password=PASSWORD, client_id=CLIENT_ID,
                  client_secret=CLIENT_SECRET, api_key=API_KEY)
    # https://apidocs.brivo.com/#filters
    users = brivo.users(filter=f"lastname__eq:{TEST_LAST_NAME}")
    assert len(users) == 1
    assert users[0]["lastName"] == TEST_LAST_NAME
