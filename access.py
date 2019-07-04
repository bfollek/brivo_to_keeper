#!/usr/bin/env python3

# Get user, pass from command line

# print expires_in

# The Legacy Application Flow works:
# https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#id9

# Header for api key? I thought it was required...
# Probably best to add it, if I can figure out how...
# Maybe it's not required to get the token. Only for calls after that?


"""
Retrieving a token with the password grant type

The same headers as mentioned above will still be required

POST
https://auth.brivo.com/oauth/token?grant_type=password&username={ADMIN_USERNAME}&password={ADMIN_PASSWORD}

Headers:
Authorization : Basic {BASE64_ENCODED_CLIENT_CREDENTIALS}
api-key       : {api-key obtained from developer.brivo.com}

An example token response

{
access_token: "[ACCESS_TOKEN_VALUE]",
token_type: "bearer",
refresh_token: "[REFRESH_TOKEN_VALUE]",
expires_in: 60
}

After an access token expires, the refresh_token can be used to request a new access_token without the need to go through the full authorization_code workflow until the refresh_token also expires.

===============================================

Refreshing a token

POST
https://auth.brivo.com/oauth/token?grant_type=refresh_token&refresh_token={REFRESH_TOKEN}

Headers:
Authorization : Basic {BASE64_ENCODED_CLIENT_CREDENTIALS}
api-key       : {api-key obtained from developer.brivo.com}

===================================================

Calls to auth.brivo.com require the following Authorization header.
Header 	Value
Authorization 	Basic CLIENT_SIGNATURE

The CLIENT_SIGNATURE is the base64 encoded concatenation of your CLIENT_ID:CLIENT_SECRET with a colon (:) delimeter.

For Example:
CLIENT_ID=ABC-123-456
CLIENT_SECRET=qwerty98765

Before Base64 Encode
ABC-123-456:qwerty98765

After encoding
QUJDLTEyMy00NTY6cXdlcnR5OTg3NjU=

===================================================

Any request that submits a request body should also include the content-type header field. It is safe to submit this with requests that do not contain a request body as well.
Header 	Value
Content-type 	application/json

"""

import os

from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

TOKEN_URL = "https://auth.brivo.com/oauth/token"

api_key = os.environ["BRIVO_API_KEY"]
client_id = os.environ["BRIVO_CLIENT_ID_PWD"]
client_secret = os.environ["BRIVO_CLIENT_SECRET_PWD"]
username = os.environ["BRIVO_USER"]
password = os.environ["BRIVO_PWD"]

oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
token = oauth.fetch_token(token_url=TOKEN_URL, username=username,
                          password=password, client_id=client_id, client_secret=client_secret)
print(token)
