from django.db import models


class BaseUser(models.Model):
    class Meta:
        abstract = True
