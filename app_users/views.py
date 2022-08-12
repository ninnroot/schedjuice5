from schedjuice5.views import BaseDetailsView, BaseListView, BaseSearchView
from .serializers import StaffSerializer
from .models import Staff


class StaffListView(BaseListView):
    name = "Staff list view"
    model = Staff
    serializer = StaffSerializer


class StaffDetailsView(BaseDetailsView):
    name = "Staff details view"
    model = Staff
    serializer = StaffSerializer


class StaffResearchView(BaseSearchView):
    name = "Staff research view"
    model = Staff
    serializer = StaffSerializer
