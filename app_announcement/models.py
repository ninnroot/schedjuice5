from django.db import models
from schedjuice5.models import BaseModel
from schedjuice5.validators import *
from app_users.models import Staff


class Announcement(BaseModel):
    title = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    body = models.TextField()
    created_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
