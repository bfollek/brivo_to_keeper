import os

from brivo import Brivo

USERNAME = os.environ["BRIVO_USERNAME"]
PASSWORD = os.environ["BRIVO_PASSWORD"]
CLIENT_ID = os.environ["BRIVO_CLIENT_ID"]
CLIENT_SECRET = os.environ["BRIVO_CLIENT_SECRET"]
API_KEY = os.environ["BRIVO_API_KEY"]


def test_brivo_token():
    brivo = Brivo(username=USERNAME, password=PASSWORD, client_id=CLIENT_ID,
                  client_secret=CLIENT_SECRET, api_key=API_KEY)
    token = brivo.token
    # Make sure we can get reasonable data out of the token
    assert int(token["expires_at"]) > 1562288222
