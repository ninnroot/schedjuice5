from schedjuice5.views import BaseDetailsView, BaseListView, BaseSearchView

from .models import *
from .serializers import *


class AnnouncementListView(BaseListView):
    name = "Announcement list view"
    serializer = AnnouncementSerializer
    model = Announcement


class AnnouncementDetailsView(BaseListView):
    name = "Announcement details view"
    serializer = AnnouncementSerializer
    model = Announcement


class AnnouncementSearchView(BaseSearchView):
    name = "Announcement search view"
    serializer = AnnouncementSerializer
    model = Announcement
