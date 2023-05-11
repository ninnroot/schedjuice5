import json
import random

import requests

from app_microsoft.graph_wrapper.base import BaseMSRequest

# The license objects' uuid never change. For quick access, they are hard-coded here.
LICENSES = {
    "staff": "94763226-9b3c-4e75-a931-5c89701abe66",
    "student": "314c4481-f395-4525-be8b-2ec4bb1e9d91",
}


class MSUser(BaseMSRequest):
    def _generate_password(self):
        password = ""
        for i in range(3):
            x1 = random.choice("abcdefghijklmnopqrstuvwxyz")
            x2 = random.choice("abcdefghijklmnopqrstuvwxyz".upper())
            x3 = random.choice("0987654321")
            x4 = random.choice("!@#$%^")
            password = password + x1 + x2 + x3 + x4
        return password

    def get(self, user_id: str):
        return super().get(f"{self.URL}users/{user_id}")

    def create(self, display_name: str, principal_name: str, password: str):
        user_payload = {
            "accountEnabled": True,
            "displayName": display_name,
            "userPrincipalName": principal_name,
            "mailNickname": principal_name.split("@")[0],
            "passwordProfile": {
                "forceChangePasswordNextSignIn": True,
                "password": password,
            },
        }
        return self.post(f"{self.URL}users", json.dumps(user_payload))

    def update_name(self, user_id: str, new_name: str):
        return self.patch(
            f"{self.URL}users/{user_id}", json.dumps({"displayName": new_name})
        )

    def enable_mail(self, user_id: str, email: str):
        payload = {"mail": email, "usageLocation": "SG"}
        return self.patch(f"{self.URL}users/{user_id}", json.dumps(payload))

    def assign_license(self, user_id: str, license_type: str):
        payload = {
            "addLicenses": [{"skuId": LICENSES[license_type]}],
            "removeLicenses": [],
        }
        return self.post(
            f"{self.URL}users/{user_id}/assignLicense", json.dumps(payload)
        )

    def delete(self, user_id: str):
        return super(MSUser, self).delete(f"{self.URL}users/{user_id}")
