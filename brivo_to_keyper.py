#!/usr/bin/env python3

import os
import sys

from brivo import Brivo


def connect_to_brivo():
    username, password = sys.argv[1:]
    client_id = os.environ["BRIVO_CLIENT_ID"]
    client_secret = os.environ["BRIVO_CLIENT_SECRET"]
    api_key = os.environ["BRIVO_API_KEY"]
    conn = Brivo(username=username, password=password,
                 client_id=client_id, client_secret=client_secret, api_key=api_key)
    return conn


if len(sys.argv) != 3:
    print("Pass your Brivo username and password on the command line.")
    sys.exit()

brivo_conn = connect_to_brivo()
brivo_token = brivo_conn.token
