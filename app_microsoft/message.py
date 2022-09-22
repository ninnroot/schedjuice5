import requests

from .auth import get_token


def getMentions(mentions):
    """
    "mentions": [
            {
                "id": 0,
                "mentionText": "Jane Smith",
                "mentioned": {
                    "user": {
                    "displayName": "Jane Smith",
                    "id": "ef1c916a-3135-4417-ba27-8eb7bd084193",
                    "userIdentityType": "aadUser"
                    }
                }
            }
        ]
    """


def getAttachments(attachments):
    """
    "attachments": [
        {
            "id": "153fa47d-18c9-4179-be08-9879815a9f90",
            "contentType": "reference",
            "contentUrl": "https://m365x987948.sharepoint.com/sites/test/Shared%20Documents/General/test%20doc.docx",
            "name": "Budget.docx"
        }
    ]
    """


def getInlineImages(inline_img):
    """
    "hostedContents":[
        {
            "@microsoft.graph.temporaryId": "1",
            "contentBytes": "",
            "contentType": "image/png"
        }
    ]
    """


def send_message_in_channel(
    message, team_id, channel_id, mentions=None, inline_img=None, attachments=None
):
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"{token['token_type']} {token['access_token']}",
    }
    data = {"body": {"contentType": "html", "content": message}}

    if mentions is not None:
        data["mentions"] = getMentions(mentions)

    if inline_img is not None:
        data["hostedContents"] = getInlineImages(inline_img)

    if attachments is not None:
        data["attachments"] = getAttachments(attachments)

    endpoint = f"https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/messages"
    res = requests.post(endpoint, headers=headers, json=data)

    return res


# ----------- DOCUMENTATION -------------
"""
    Parameters of send_message_in_channel():

    How to test function:
        team_id = "31c0e1ed-127f-4257-9eb8-33ae118128a3"
        channel_id = "19:03501f2680404d14a259ca260f4bc6e1@thread.tacv2"
        res = send_message_in_channel("<h1>Hello World</h1>", team_id, channel_id)
"""
