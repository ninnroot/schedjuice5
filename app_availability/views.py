from django.core.exceptions import BadRequest
from django.db.models import Q
from rest_framework.views import Request
from utilitas.views import BaseView

from app_course.models import Course, Event
from app_course.serializers import CourseSerializer, EventSerializer
from app_users.models import Staff
from app_users.serializers import StaffSerializer


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
            try:
                self.sorts = self.get_sort_param(request)
                self.expand = self.get_expand_param(request)
                self.fields = self.get_field_filter_param(request)
            except BadRequest as e:
                return self.send_response(
                    True, "bad_request", {"details": str(e)}, status=400
                )
            # The staff's existing assigned events
            assigned_events = staff.staffs_events.prefetch_related("event").all()

            # From event table, get events of which dates are in the 'assigned_events' set
            same_day_events = (
                Event.objects.filter(date__in=[i.event.date for i in assigned_events])
                .exclude(id__in=[i.event.id for i in assigned_events])
                .all()
            )

            # The timeslots (events) that the staff is not free for.
            # Obviously, they will include the staff's original assigned events
            not_free = [i.event.id for i in assigned_events]
            for i in assigned_events:
                # Iterate through each day that the staff has events on,
                # get events of the same date from 'same_day_events' set.
                # Then, check if the events are colliding.
                # If yes, append to 'not_free' set.
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

            # temporary fix :)
            course_id = request.query_params.get("course")
            if course_id:
                course = Course.objects.filter(pk=course_id).first()
                if not course:
                    return self.send_response(
                        True,
                        "not_found",
                        {"details": f"Course with id {obj_id} does not exist."},
                    )
                all_events = (
                    Event.objects.filter(course_id=course_id)
                    .all()
                    .order_by(*self.sorts)
                )
                serialized_data = self.get_serializer(
                    self.paginate_queryset(all_events, request),
                    many=True,
                    expand=self.expand,
                    fields=self.fields,
                )
                for i in serialized_data.data:
                    if i["id"] in not_free:
                        i["is_free"] = False
                    else:
                        i["is_free"] = True

                return self.send_response(
                    False,
                    "all_good",
                    {**self.get_paginated_response(), "data": serialized_data.data},
                )

            # 'free_events' set is just the compliment of the 'not_free' set.
            free_events = (
                Event.objects.exclude(id__in=not_free).all().order_by(*self.sorts)
            )

            serialized_data = self.get_serializer(
                self.paginate_queryset(free_events, request),
                many=True,
                expand=self.expand,
                fields=self.fields,
            )

            return self.send_response(
                False,
                "all_good",
                {**self.get_paginated_response(), "data": serialized_data.data},
            )

        elif model == "event":
            event = Event.objects.filter(pk=obj_id).first()
            if event is None:
                return self.send_response(
                    True,
                    "not_found",
                    {"details": f"Event with id {obj_id} does not exist."},
                )

            self.serializer = StaffSerializer
            self.model = Staff
            try:
                self.sorts = self.get_sort_param(request)
                self.expand = self.get_expand_param(request)
                self.fields = self.get_field_filter_param(request)
            except BadRequest as e:
                return self.send_response(
                    True, "bad_request", {"details": str(e)}, status=400
                )

            colliding_events = (
                Event.objects.filter(date=event.date)
                .exclude(
                    (Q(time_from__gte=event.time_to) or Q(time_to__lte=event.time_from))
                )
                .all()
            )
            free_staffs = (
                Staff.objects.exclude(
                    staffs_events__event__id__in=[i.id for i in colliding_events]
                )
                .prefetch_related("staffs_events__event")
                .all()
            )
            serialized_data = self.get_serializer(
                self.paginate_queryset(free_staffs, request),
                many=True,
                expand=self.expand,
                fields=self.fields,
            )
            return self.send_response(
                False,
                "all_good",
                {**self.get_paginated_response(), "data": serialized_data.data},
            )

        elif model == "course":
            course = Course.objects.filter(pk=obj_id).first()
            if course is None:
                return self.send_response(
                    True,
                    "not_found",
                    {"details": f"Course with id {obj_id} does not exist."},
                )

            self.serializer = StaffSerializer
            self.model = Staff
            try:
                self.sorts = self.get_sort_param(request)
                self.expand = self.get_expand_param(request)
                self.fields = self.get_field_filter_param(request)
            except BadRequest as e:
                return self.send_response(
                    True, "bad_request", {"details": str(e)}, status=400
                )

            course_events = (
                Event.objects.filter(course__id=course.id).order_by("date").all()
            )
            colliding_events = [i for i in course_events]

            if len(course_events) != 0:
                start_date, end_date = (
                    course_events.first().date,
                    course_events.last().date,
                )
                start_time = course_events.order_by("time_from").first().time_from
                end_time = course_events.order_by("time_to").last().time_to

                event_subset = (
                    Event.objects.exclude(id__in=[i.id for i in course_events])
                    .filter(date__gte=start_date, date__lte=end_date)
                    .exclude(Q(time_from__gte=end_time) | Q(time_to__lte=start_time))
                    .all()
                )
                events_grouped_by_date = {}

                for i in event_subset:
                    if i.date not in events_grouped_by_date:
                        events_grouped_by_date[i.date] = [i]
                    else:

                        events_grouped_by_date[i.date].append(i)

                for i in course_events:
                    if i.date not in events_grouped_by_date:
                        continue
                    for j in events_grouped_by_date[i.date]:
                        if not (i.time_from >= j.time_to or i.time_to <= j.time_from):
                            colliding_events.append(j)

            free_staffs = (
                Staff.objects.exclude(
                    staffs_events__event__id__in=[i.id for i in colliding_events]
                )
                .prefetch_related("staffs_events__event")
                .all()
            )
            serialized_data = self.get_serializer(
                self.paginate_queryset(free_staffs, request),
                many=True,
                expand=self.expand,
                fields=self.fields,
            )
            return self.send_response(
                False,
                "all_good",
                {**self.get_paginated_response(), "data": serialized_data.data},
            )

        return self.send_response(
            True, "Available models are 'staff', 'event' or 'course'", {}, status=404
        )
