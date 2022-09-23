from schedjuice5.views import BaseDetailsView, BaseListView, BaseSearchView

from .models import *
from .serializers import *


# ------------ VenueClassification Section ------------
class VenueClassificationListView(BaseListView):
    name = "VenueClassification list view"
    model = VenueClassification
    serializer = VenueClassificationSerializer


class VenueClassificationDetailsView(BaseDetailsView):
    name = "VenueClassification details view"
    model = VenueClassification
    serializer = VenueClassificationSerializer


class VenueClassificationSearchView(BaseSearchView):
    name = "VenueClassification search view"
    model = VenueClassification
    serializer = VenueClassificationSerializer


# ------------ Campus Section ------------
class CampusListView(BaseListView):
    name = "Campus list view"
    model = Campus
    serializer = CampusSerializer


class CampusDetailsView(BaseDetailsView):
    name = "Campus details view"
    model = Campus
    serializer = CampusSerializer


class CampusSearchView(BaseSearchView):
    name = "Campus search view"
    model = Campus
    serializer = CampusSerializer


# ------------ Venue Section ------------
class VenueListView(BaseListView):
    name = "Venue list view"
    model = Venue
    serializer = VenueSerializer


class VenueDetailsView(BaseDetailsView):
    name = "Venue details view"
    model = Venue
    serializer = VenueSerializer


class VenueSearchView(BaseSearchView):
    name = "Venue search view"
    model = Venue
    serializer = VenueSerializer
