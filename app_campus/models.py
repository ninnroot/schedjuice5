from django.db import models
from rest_framework.serializers import ValidationError
from utilitas.models import BaseModel

from app_utils.choices.country_codes import country_codes
from schedjuice5.validators import *


class VenueClassification(BaseModel):
    """
    Represents a type of Venue.
    """

    name = models.CharField(max_length=256, validators=[nameValidation])
    description = models.TextField(default="...")


class Campus(BaseModel):
    """
    Represents a collection of Venues. A physical location. A Campus can contain many Venues.
    """

    name = models.CharField(max_length=256, validators=[nameWithNumberValidation])
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
    country = models.CharField(max_length=64, choices=country_codes)
    postal_code = models.CharField(max_length=16, validators=[strictNumberValidation])

    def save(self, *args, **kwargs):
        if self.opening_time >= self.closing_time:
            raise ValidationError(
                "opening_time cannot be greater than or equal to closing_time"
            )

        return super().save(*args, **kwargs)


class Venue(BaseModel):
    """
    A physical location where physical Events can take place. A Venue may belong to one and only one Campus.
    """

    code = models.CharField(
        max_length=64,
        validators=[usernameValidation],
        help_text="A short standardized code.",
    )
    location = models.CharField(
        max_length=64,
        validators=[englishAndSomeSpecialValidation],
        help_text="The location of the Venue in a certain Campus. For example, room and floor number.",
    )

    classification = models.ForeignKey(
        VenueClassification,
        on_delete=models.PROTECT,
        null=True,
        help_text="Type of the Venue.",
        related_name="venues",
    )
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        null=True,
        help_text="The Campus that the Venue is located within.",
        related_name="venues",
    )

    class Meta:
        unique_together = ("code", "campus")
