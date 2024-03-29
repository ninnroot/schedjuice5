from django.db import models
from rest_framework.serializers import ValidationError
from utilitas.models import BaseModel

from app_campus.models import Venue
from schedjuice5.validators import *


class Category(BaseModel):
    """
    A Category is a collection of Courses. A Category can contain many Courses.
    """

    name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation], unique=True
    )
    description = models.TextField(default="...")


class Course(BaseModel):
    """
    One of the fundamental models in the API. Staff can be assigned and Students can be enrolled to a Course.
    A Course may belong to one and only one Category, and a Course can contain many Events.
    """

    COURSE_TYPE = (("on_campus", "On Campus"), ("online", "Online"))

    name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation], unique=True
    )
    description = models.TextField(default="...")
    code = models.CharField(
        max_length=64,
        validators=[usernameValidation],
        unique=True,
        help_text="A short standardized code.",
    )
    start_date = models.DateField(help_text="The course starting date.")
    end_date = models.DateField(help_text="The course ending date.")
    monthly_fee = models.PositiveIntegerField()
    color = models.CharField(
        max_length=50, default="#FA7070", validators=[colorCodeValidation]
    )
    course_type = models.CharField(choices=COURSE_TYPE, default="online", max_length=10)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="courses"
    )

    def save(self, *args, **kwargs):
        if self.start_date >= self.end_date:
            raise ValidationError(
                "start_date cannot be greater than or equal to end_date."
            )
        return super().save(*args, **kwargs)


class Event(BaseModel):
    """
    An Event manifests in the real world, and it can consume finite resources such as
    time and space, though the latter is optional. Once an Event is initialized, it consumes
    the time and space resources that it has been assigned to.
    """

    event_types = [
        ("lecture",) * 2,
        ("holiday",) * 2,
        ("exam",) * 2,
        ("other",) * 2,
    ]

    name = models.CharField(
        max_length=100,
        validators=[englishAndSomeSpecialValidation],
        default="T.Su Event",
    )
    date = models.DateField(help_text="The date that the event falls onto.")
    time_from = models.TimeField(help_text="Starting time of the event.")
    time_to = models.TimeField(help_text="Ending time of the event.")

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="events")
    classification = models.CharField(max_length=128, choices=event_types)

    def save(self, *args, **kwargs):
        if self.time_to <= self.time_from:
            raise ValidationError("time_to cannot be less than or equal to time_from.")

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}-{self.date}-{self.time_from}-{self.time_to}"


class EventVenue(BaseModel):
    """
    The bridge table for the Event and Venue models.
    """

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="events_venues"
    )
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name="events_venues"
    )


class Calendar(BaseModel):
    """
    A Calendar stores ranges of dates which can be used to create many Events. Calendars can be used to save particular
    configuration of Events.
    """

    name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation], unique=True
    )
    config = models.JSONField(help_text="Event configuration saved in the json format.")
