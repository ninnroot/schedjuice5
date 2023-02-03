from django.db.models import Q
from rest_framework.views import Request

from app_course.models import Event
from app_course.serializers import EventSerializer
from app_users.models import Staff
from app_users.serializers import StaffSerializer
from schedjuice5.views import BaseView


class AvailabilityView(BaseView):
    name = "list of availabilities"

    def get(self, request: Request, model: str, obj_id: int):
        model = model.lower()
        if model == "staff":
            staff = Staff.objects.filter(pk=obj_id).first()
            if staff is None:
                return self.send_response(
                    True,
                    "not_found",
                    {"details": f"Staff with id {obj_id} does not exist."},
                )

            self.serializer = EventSerializer
            self.model = Event

            # the staff's existing assigned events
            assigned_events = staff.staffs_events.prefetch_related("event").all()

            # from event table, get events which date are in the 'assigned_events' set
            same_day_events = (
                Event.objects.filter(date__in=[i.event.date for i in assigned_events])
                .exclude(id__in=[i.event.id for i in assigned_events])
                .all()
            )

            # the timeslots (events) that the staff is not free. Obviously, they will include the staff's original assigned events
            not_free = [i.event.id for i in assigned_events]
            for i in assigned_events:
                # iterate through each day that the staff has events on. Then, check if the events are colliding. If yes, then, append to 'not_free' set.
                not_free.extend(
                    [
                        x.id
                        for x in same_day_events
                        if x.date == i.event.date
                        and (
                            x.time_from > i.event.time_to
                            or x.time_to < i.event.time_from
                        )
                    ]
                )

            # 'free_events' set is just the compliment of the 'not_free' set.
            free_events = Event.objects.exclude(id__in=not_free).all()

            serialized_data = self.get_serializer(
                self.paginate_queryset(free_events, request), many=True
            )
            return self.send_response(
                False,
                "all_good",
                {**self.get_paginated_response(), "events": serialized_data.data},
            )

        elif model == "event":
            print("event")
        elif model == "course":
            print("course")

        return self.send_response(
            True, "Available models are 'staff', 'event' or 'course'", {}, status=404
        )
