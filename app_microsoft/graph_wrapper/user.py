import json
import random

import requests

from app_microsoft.graph_wrapper.base import BaseMSRequest


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
        print(self._generate_password())
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
