import json
from datetime import datetime

import pytz

from app_microsoft.graph_wrapper.base import STAFFY_ID, BaseMSRequest


class MSGroup(BaseMSRequest):
    member_settings = {
        "allowCreateUpdateChannels": False,
        "allowDeleteChannels": False,
        "allowAddRemoveApps": False,
        "allowCreateUpdateRemoveTabs": False,
        "allowCreateUpdateRemoveConnectors": False,
    }

    def make_channel(self, name, is_favourite=True):
        return {"displayName": name, "isFavouriteByDefault": is_favourite}

    def create(self, name, group_type="educationClass"):
        payload = {
            "template@odata.bind": f"https://graph.microsoft.com/v1.0/teamsTemplates('{group_type}')",
            "displayName": name,
            "description": f"Hello, welcome to {name}. Created by Schedjuice5 at {datetime.now(tz=pytz.timezone('Asia/Rangoon'))}",
            "channels": [self.make_channel("General")],
            "mailEnabled": False,
            "memberSettings": self.member_settings,
            "owners@odata.bind": [
                "https://graph.microsoft.com/v1.0/users/" + STAFFY_ID
            ],
        }
        return self.post(f"{self.BETA_URL}teams", json.dumps(payload))

    def add_channel(self, group_id: str, channel_name: str, is_favourite=True):
        return self.post(
            f"{self.URL}teams/{group_id}/channels",
            json.dumps(self.make_channel(channel_name, is_favourite)),
        )

    def add_member(self, user_id: str, group_id: str, role: str):
        payload = {}
        if role == "owners":
            payload = {"@odata.id": "https://graph.microsoft.com/v1.0/users/" + user_id}

        elif role == "members":
            payload = {
                "@odata.id": "https://graph.microsoft.com/v1.0/directoryObjects/"
                + user_id
            }

        return self.post(
            f"{self.URL}groups/{group_id}/{role}/$ref", json.dumps(payload)
        )

    def remove_member(self, group_id: str, user_id: str, role: str):
        return super(MSGroup, self).delete(
            f"{self.URL}groups/{group_id}/{role}/{user_id}/$ref"
        )

    def delete(self, group_id: str):
        return super(MSGroup, self).delete(f"{self.URL}groups/{group_id}")
