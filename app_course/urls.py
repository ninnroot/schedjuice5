from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "categories/<int:obj_id>/",
        views.CategoryDetailsView.as_view(),
        name="category_details",
    ),
    path(
        "categories/search/", views.CategorySearchView.as_view(), name="category_search"
    ),
    path(
        "eventclassifications/",
        views.EventClassificationListView.as_view(),
        name="eventclassification_list",
    ),
    path(
        "eventclassifications/<int:obj_id>/",
        views.EventClassificationDetailsView.as_view(),
        name="eventclassification_details",
    ),
    path(
        "eventclassifications/search/",
        views.EventClassificationSearchView.as_view(),
        name="eventclassification_search",
    ),
    path("courses/", views.CourseListView.as_view(), name="course_list"),
    path(
        "courses/<int:obj_id>/",
        views.CourseDetailsView.as_view(),
        name="course_details",
    ),
    path("courses/search/", views.CourseSearchView.as_view(), name="course_search"),
    path("events/", views.EventListView.as_view(), name="event_list"),
    path(
        "events/<int:obj_id>/", views.EventDetailsView.as_view(), name="event_details"
    ),
    path("events/search/", views.EventSearchView.as_view(), name="event_search"),
    path("event-venues/", views.EventVenueListView.as_view(), name="eventvenue_list"),
    path(
        "event-venues/<int:obj_id>/",
        views.EventVenueDetailsView.as_view(),
        name="eventvenue_details",
    ),
    path(
        "event-venues/search/",
        views.EventVenueSearchView.as_view(),
        name="eventvenue_search",
    ),
    path("calendars/", views.CalendarListView.as_view(), name="calendar_list"),
    path(
        "calendars/<int:obj_id>/",
        views.CalendarDetailsView.as_view(),
        name="calendar_details",
    ),
    path(
        "calendars/search/", views.CalendarSearchView.as_view(), name="calendar_search"
    ),
]
