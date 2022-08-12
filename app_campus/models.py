from app_utils.choices import countries
from schedjuice5.models import BaseModel
from schedjuice5.validators import *

from django.db import models
from rest_framework.serializers import ValidationError


class VenueClassification(BaseModel):
    name = models.CharField(max_length=256, validators=[nameValidation])
    description = models.TextField()


class Campus(BaseModel):

    name = models.CharField(
        max_length=256, validators=[nameWithNumberValidation], unique=True
    )
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    house_number = models.CharField(
        max_length=16, validators=[englishAndSomeSpecialValidation]
    )
    block_number = models.CharField(
        max_length=16, validators=[englishAndSomeSpecialValidation], null=True
    )
    street_name = models.CharField(max_length=32, validators=[nameWithNumberValidation])
    township = models.CharField(max_length=32, validators=[nameWithNumberValidation])
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64, choices=countries)
    postal_code = models.CharField(max_length=16, validators=[strictNumberValidation])

    def save(self, *args, **kwargs):
        if self.opening_time >= self.closing_time:
            raise ValidationError(
                "opening_time cannot be greater than or equal to closing_time"
            )

        return super().save(*args, **kwargs)


class Venue(BaseModel):
    code = models.CharField(max_length=64, validators=[usernameValidation])
    location = models.CharField(
        max_length=64, validators=[englishAndSomeSpecialValidation]
    )

    classification = models.ForeignKey(VenueClassification, on_delete=models.PROTECT)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("campus", "code")
