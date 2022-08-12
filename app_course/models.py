from schedjuice5.models import BaseModel
from django.db import models
from schedjuice5.validators import *
from rest_framework.serializers import ValidationError

from app_campus.models import Venue


class Category(BaseModel):

    name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    description = models.TextField()


class EventClassification(BaseModel):
    name = models.CharField(max_length=256, validators=[nameValidation])
    description = models.TextField()


class Course(BaseModel):

    name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    description = models.TextField()
    code = models.CharField(max_length=64, validators=[usernameValidation])
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_fee = models.PositiveIntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.end_date >= self.start_date:
            raise ValidationError(
                "end_date cannot be greater than or equal to start_date."
            )
        return super().save(*args, **kwargs)


class Event(BaseModel):

    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()

    classification = models.ForeignKey(EventClassification, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if self.time_to >= self.time_from:
            raise ValidationError("time_to cannot be greater than or equal to time_to.")

        return super().save(*args, **kwargs)


class EventVenue(BaseModel):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)


class Calendar(BaseModel):

    name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    config = models.JSONField()
