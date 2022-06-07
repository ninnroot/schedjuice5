from tkinter.tix import Tree
from suconnect_1.models import BaseModel
from django.db import models


class Record(BaseModel):

    name = models.CharField(max_length=256, unique=True)

