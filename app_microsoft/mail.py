import requests
import os
import base64
from .auth import get_token

base_url = "https://graph.microsoft.com/v1.0/me/sendMail"

def file_attachment(file_path, is_inline=False):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            content = base64.b64encode(f.read())
        data_body = {
            "@odata.type": "#microsoft.graph.fileAttachment",
            "contentBytes": content.decode("utf-8"),
            "name": os.path.basename(file_path),
            "isInline": is_inline
        }
        return data_body

    return None

def item_attachment(body, subject, start, end, is_inline=False):
    data_body = {
        "@odata.type": "#microsoft.graph.itemAttachment",
        "item": {
            "@odata.type": "microsoft.graph.event",
            "body": {
                "contentType": "HTML",
                "content": body
            },
            "subject": subject,
            "start": {
                "dateTime": start,
                "timeZone": "Pacific Standard Time"
            },
            "end": {
                "dateTime": end,
                "timeZone": "Pacific Standard Time"   
            }
        },
        "isInline": is_inline
    }
    return data_body

def send_mail(subject, body, to, cc=None, bcc=None, attachments=None, start=None, end=None, item=None, item_subject=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(get_token())
    }
    data = {
        "subject": subject,
        "body": {
            "contentType": "HTML",
            "content": body
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "address": to
                }
            }
        ],
        "ccRecipients": [
            {
                "emailAddress": {
                    "address": cc
                }
            }
        ],
        "bccRecipients": [
            {
                "emailAddress": {
                    "address": bcc
                }
            }
        ],
        "attachments": [
            file_attachment(attachments, is_inline=False),
            item_attachment(item, item_subject, start, end, is_inline=True)
        ],
    }
    r = requests.post(base_url, headers=headers, json=data)
    return r.status_code == requests.codes.ok


is_sent = send_mail("Test", "Test", "to.72.72.78.111@gmail.com")
print(is_sent)