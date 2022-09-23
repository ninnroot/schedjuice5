import decouple
import requests

from .auth import get_token

USER_ID = decouple.config("USER_ID")


def create_team():
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"{token['token_type']} {token['access_token']}",
    }
    data = {
        "template@odata.bind": "https://graph.microsoft.com/v1.0/teamsTemplates('standard')",
        "displayName": "Guru's Team",
        "description": "test test test",
        "channels": [
            {
                "displayName": "Announcements 📢",
                "isFavoriteByDefault": True,
                "description": "This is a sample announcements channel that is favorited by default. Use this channel to make important team, product, and service announcements.",
            }
        ],
        "members": [
            {
                "@odata.type": "#microsoft.graph.aadUserConversationMember",
                "roles": ["owner"],
                "user@odata.bind": f"https://graph.microsoft.com/v1.0/users('{USER_ID}')",
            }
        ],
    }

    endpoint = "https://graph.microsoft.com/v1.0/teams"
    res = requests.post(endpoint, headers=headers, json=data)

    return res


def list_teams():
    pass
