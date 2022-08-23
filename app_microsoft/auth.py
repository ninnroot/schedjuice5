import decouple
import msal
from .scopes import scopes

TENANT = decouple.config("MS_AUTHORITY")
CLIENT_ID = decouple.config("APP_ID")
KEY = decouple.config("KEY")
THUMBPRINT = decouple.config("THUMBPRINT")


def get_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority="https://login.microsoftonline.com/" + TENANT,
        client_credential={"thumbprint": THUMBPRINT, "private_key": open(KEY).read()},
    )
    # return app
    x = app.acquire_token_silent(scopes, account=None)
    if not x:
        res = x.aquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

        return res
    return x
