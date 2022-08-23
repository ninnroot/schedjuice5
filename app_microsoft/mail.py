import requests
import os
import base64
from .auth import get_token
# from .scopes import my_access_token

base_url = "https://graph.microsoft.com/v1.0/me/sendMail"

def file_attachment(attachment, is_inline):
    try:
        with open(attachment, "rb") as f:
            content = base64.b64encode(f.read())
        data_body = {
            "@odata.type": "#microsoft.graph.fileAttachment",
            "contentBytes": content.decode("utf-8"),
            "name": os.path.basename(attachment),
            "isInline": is_inline
        }
        return data_body
    except FileNotFoundError:
        raise Exception("File not Found")

    
def getRecipients(recipients):
    return [
        {
            "emailAddress": {
                "address": recipient
            }
        }
        for recipient in recipients
    ]


def getAttachments(attachments):
    
    return [
        file_attachment(attachment[0], attachment[1])
            for attachment in attachments 
    ]


def send_mail(subject, body, to, cc=None, bcc=None, attachments=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_token()}"
    }
    data = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "HTML",
                "content": body
            },
            "toRecipients": getRecipients(to),
        }
    }

    if cc is not None:
        data["message"]["ccRecipients"] = getRecipients(cc)

    if bcc is not None:
        data["message"]["bccRecipients"] = getRecipients(bcc)

    if attachments is not None:
        data["message"]["attachments"] = getAttachments(attachments)


    r = requests.post(base_url, headers=headers, json=data)
    return (data, r)


"""
    Parameters of send_mail()
        subject: str
        body: str(html or txt)
        to: list => ["test@gmail.com", "admin@gmail.com"]
        cc: list => ["test@gmail.com", "admin@gmail.com"]
        bcc: list => ["test@gmail.com", "admin@gmail.com"]
        attachments: list of tuples => [("file.txt", False), ("img.png", True)]

    return format: (data, response)

    to test function: send_mail("Test", "Test", ["to.72.72.78.111@gmail.com"], attachments=[("attachment.txt", False)])
"""