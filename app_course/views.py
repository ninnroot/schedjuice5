from utilitas.views import BaseDetailsView, BaseListView, BaseSearchView

from .models import *
from .serializers import *


# ------------ Category Section ------------
class CategoryListView(BaseListView):
    name = "Category list view"
    model = Category
    serializer = CategorySerializer


class CategoryDetailsView(BaseDetailsView):
    name = "Category details view"
    model = Category
    serializer = CategorySerializer


class CategorySearchView(BaseSearchView):
    name = "Category search view"
    model = Category
    serializer = CategorySerializer


# ------------ Course Section ------------
class CourseListView(BaseListView):
    name = "Course list view"
    model = Course
    serializer = CourseSerializer


class CourseDetailsView(BaseDetailsView):
    name = "Course details view"
    model = Course
    serializer = CourseSerializer


class CourseSearchView(BaseSearchView):
    name = "Course search view"
    model = Course
    serializer = CourseSerializer


# ------------ Event Section ------------
class EventListView(BaseListView):
    name = "Event list view"
    model = Event
    serializer = EventSerializer
    related_fields = [
        "staffs_events__staff",
        "staffs_events__event",
        "staffs_events__job",
    ]


class EventDetailsView(BaseDetailsView):
    name = "Event details view"
    model = Event
    serializer = EventSerializer


class EventSearchView(BaseSearchView):
    name = "Event search view"
    model = Event
    serializer = EventSerializer


# ------------ EventVenue Section ------------
class EventVenueListView(BaseListView):
    name = "EventVenue list view"
    model = EventVenue
    serializer = EventVenueSerializer


class EventVenueDetailsView(BaseDetailsView):
    name = "EventVenue details view"
    model = EventVenue
    serializer = EventVenueSerializer


class EventVenueSearchView(BaseSearchView):
    name = "EventVenue search view"
    model = EventVenue
    serializer = EventVenueSerializer


# ------------ Calendar Section ------------
class CalendarListView(BaseListView):
    name = "Calendar list view"
    model = Calendar
    serializer = CalendarSerializer


class CalendarDetailsView(BaseDetailsView):
    name = "Calendar details view"
    model = Calendar
    serializer = CalendarSerializer


class CalendarSearchView(BaseSearchView):
    name = "Calendar search view"
    model = Calendar
    serializer = CalendarSerializer
