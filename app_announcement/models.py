from django.db import models

from app_users.models import Staff
from schedjuice5.models import BaseModel
from schedjuice5.validators import *


class Announcement(BaseModel):
    title = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    body = models.TextField()
    created_by = models.ForeignKey(
        Staff, on_delete=models.SET_NULL, related_name="announcements", null=True
    )


class Attachment(BaseModel):
    attachment_file = models.FileField(upload_to="announcements")
    announcement = models.ForeignKey(
        Announcement, on_delete=models.CASCADE, related_name="attachments"
    )
