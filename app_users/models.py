from django.db import models
from schedjuice5.models import BaseModel
from app_auth.models import Account


class BaseUser(BaseModel):
    username = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    about = models.TextField()
    dob = models.DateField()
    secondary_email = models.EmailField()
    gender = models.CharField(max_length=128)

    class Meta:
        abstract = True


class Staff(BaseUser):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
