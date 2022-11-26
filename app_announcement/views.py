from schedjuice5.views import BaseDetailsView, BaseListView, BaseSearchView

from .models import *
from .serializers import *

# ------------- Announcement ------------- #
class AnnouncementListView(BaseListView):
    name = "Announcement list view"
    serializer = AnnouncementSerializer
    model = Announcement


class AnnouncementDetailsView(BaseDetailsView):
    name = "Announcement details view"
    serializer = AnnouncementSerializer
    model = Announcement


class AnnouncementSearchView(BaseSearchView):
    name = "Announcement search view"
    serializer = AnnouncementSerializer
    model = Announcement
    
    
# -------------- Attachment --------------- #
class AttachmentListView(BaseListView):
    name = "Attachment list view"
    serializer = AttachmentSerializer
    model = Attachment


class AttachmentDetailsView(BaseDetailsView):
    name = "Attachment details view"
    serializer = AttachmentSerializer
    model = Attachment


class AttachmentSearchView(BaseSearchView):
    name = "Attachment search view"
    serializer = AttachmentSerializer
    model = Attachment
