from schedjuice5.models import BaseModel
from schedjuice5.validators import *

from app_users.models import Staff
from django.db import models


class Group(BaseModel):

    name = models.CharField(max_length=256, validators=[nameValidation])
    description = models.TextField()
    parent_id = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)


class StaffGroup(BaseModel):

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
