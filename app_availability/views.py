from rest_framework.views import Request

from app_course.models import Event
from app_course.serializers import EventSerializer
from app_users.models import Staff
from app_users.serializers import StaffSerializer
from schedjuice5.views import BaseView


class AvailabilityView(BaseView):
    name = "list of availabilities"

    def get(self, request: Request, model: str, obj_id: int):
        if model == "staff":
            self.model = Staff
            staff = self._get_object(obj_id)
            if staff is None:
                return self._send_not_found(obj_id)
            assigned_events = staff.staffs_events
            print(assigned_events)
            return self.send_response(False, "all good", {})

        elif model == "event":
            print("event")
        elif model == "course":
            print("course")

        return self.send_response(
            True, "Available models are 'staff', 'event' or 'course'", {}, status=404
        )
