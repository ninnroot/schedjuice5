from django.db import models
from schedjuice5.models import BaseModel
from app_auth.models import Account


class Staff(BaseModel):
    name = models.CharField(max_length=256)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
