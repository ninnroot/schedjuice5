from schedjuice5.views import BaseDetailsView, BaseListView
from .models import Staff
from .serializers import StaffSerializer

# Create your views here.
class StaffListView(BaseListView):
    name = "Staff list view"
    model = Staff
    serializer = StaffSerializer


class StaffDetailsView(BaseDetailsView):
    name = "Staff details view" 
    model = Staff
    serializer = StaffSerializer