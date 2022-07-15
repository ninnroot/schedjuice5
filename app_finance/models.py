from suconnect_1.models import BaseModel
from django.db import models


class Record(BaseModel):
    """
    The Record object is one of the fundamental models in this API.

    A Record object represents a transaction uploaded by a client.
    The initial status of the Record will be "processing", and once an admin
    has made a decision, it will change to "approved" or "declined" respectively.

    """

    name = models.CharField(
        max_length=256, unique=True, help_text="the name of the record"
    )
    status = models.CharField(
        max_length=256,
        help_text="status will be in the list of ['processing','approved','declined']",
    )
    bank_type = models.CharField(
        max_length=256,
        help_text="the type of the bank used to made the transaction. "
        "it will be in the list of ['KBZ', 'AYA', 'CB', 'KBZ_Pay']",
    )
    amount = models.IntegerField(help_text="the monetary value of the transaction.")
    approved_on = models.DateTimeField(
        null=True, help_text="the date of approval made by an admin."
    )
