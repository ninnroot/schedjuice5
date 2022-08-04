from django.utils.decorators import method_decorator

from rest_framework.views import Request

from drf_yasg.utils import swagger_auto_schema

from schedjuice5.views import BaseDetailsView, BaseListView
from .models import Staff
from .serializers import StaffSerializer

# Create your views here.
# @method_decorator(decorator=swagger_auto_schema(request_body=StaffSerializer), name='post')
class StaffListView(BaseListView):
    name = "Staff list view"
    model = Staff
    serializer = StaffSerializer

    # for adding request body in swagger, we need to decorate the view with @swagger_auto_schema
    @swagger_auto_schema(request_body=serializer)
    def post(self, request: Request):
        return super().post(request)



class StaffDetailsView(BaseDetailsView):
    name = "Staff details view" 
    model = Staff
    serializer = StaffSerializer

    # for adding request body in swagger, we need to decorate the view with @swagger_auto_schema
    @swagger_auto_schema(request_body=serializer)
    def put(self, request: Request, obj_id: int):
        return super().put(request, obj_id)
