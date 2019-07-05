from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

TOKEN_URL = "https://auth.brivo.com/oauth/token"


class Brivo:

    def __init__(self, username, password, client_id, client_secret, api_key):
        self._username = username
        self._password = password
        self._client_id = client_id
        self._client_secret = client_secret
        self._api_key = api_key

    @property
    def token(self):
        oauth = OAuth2Session(
            client=LegacyApplicationClient(client_id=self._client_id))
        token = oauth.fetch_token(token_url=TOKEN_URL, username=self._username,
                                  password=self._password, client_id=self._client_id, client_secret=self._client_secret)
        return token
