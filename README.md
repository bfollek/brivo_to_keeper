# brivo_to_keeper

A utility to transfer user data from Brivo to Keyper

This is a work-in-progress. It will eventually transfer user data from a [Brivo](https://www.brivo.com/) system to a [Keyper](https://www.keypersystems.com/) system.

Currently, **brivo.py** is working. See **test_brivo.py** for usage info.

#### brivo. py - Notes/Limitations

* Provides only the [user list](https://apidocs.brivo.com/#api-User-ListUsers) api
* Uses the Oauth2 **password** grant type. It's designed to run as a stand-alone program, not as part of a webapp.
* Doesn't use the refresh token.