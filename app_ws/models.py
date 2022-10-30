from django.db import models

from schedjuice5.models import BaseModel


class TestChannel(BaseModel):
    name = models.CharField(max_length=256)
    req_id = models.CharField(max_length=256)
