from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import requests

TOKEN_URL = "https://auth.brivo.com/oauth/token"
USERS_URL = "https://api.brivo.com/v1/api/users"


class Brivo:

    def __init__(self, username, password, client_id, client_secret, api_key):
        # Connect and get an access token
        client = LegacyApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)
        # oauth = OAuth2Session(
        #     client=LegacyApplicationClient(client_id=client_id))
        self._token = oauth.fetch_token(token_url=TOKEN_URL, username=username,
                                        password=password, client_id=client_id, client_secret=client_secret)
        # Set up the headers we'll need for each request
        self._request_headers = {"api-key": api_key,
                                 "Authorization": f"bearer {self._token['access_token']}",
                                 "Content-type": "application/json"}

    def users(self, **optional_fields):
        """
        Returns the list of users. Each user is a dictionary of field/value items.
        Use optional_fields to pass any of the optional querystring params.
        See https://apidocs.brivo.com/#api-User-ListUsers
        """
        r = requests.get(
            USERS_URL, headers=self._request_headers, params=optional_fields)
        r.raise_for_status()
        return r.json()['data']
