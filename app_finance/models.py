from suconnect_1.models import BaseModel
from django.db import models


class Record(BaseModel):

    name = models.CharField(
        max_length=256, unique=True, 
        help_text="the name of the record"
        )
    status = models.CharField(
        max_length=256,
        help_text="status will be in the list of ['not_accepting','accepting','processing','approved','declined']"
        )
    bank_type = models.CharField(max_length=256)
    amount = models.IntegerField()
    approved_on = models.DateTimeField(null=True)

