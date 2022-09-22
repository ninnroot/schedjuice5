from django.urls import path

from . import views

urlpatterns = [
    path("groups/", views.GroupListView.as_view(), name="group-list"),
    path("groups/<int:obj_id>/", views.GroupDetailsView.as_view(), name="group-detail"),
    path("groups/search/", views.GroupSearchView.as_view(), name="group-search"),
    path("departments/", views.DepartmentListView.as_view(), name="department-list"),
    path(
        "departments/<int:obj_id>/",
        views.DepartmentDetailsView.as_view(),
        name="department-detail",
    ),
    path(
        "departments/search/",
        views.DepartmentSearchView.as_view(),
        name="department-search",
    ),
    path("jobs/", views.JobListView.as_view(), name="job-list"),
    path("jobs/<int:obj_id>/", views.JobDetailsView.as_view(), name="job-detail"),
    path("jobs/search/", views.JobSearchView.as_view(), name="job-search"),
    path("roles/", views.RoleListView.as_view(), name="role-list"),
    path("roles/<int:obj_id>/", views.RoleDetailsView.as_view(), name="role-detail"),
    path("roles/search/", views.RoleSearchView.as_view(), name="role-search"),
    path("permissions/", views.PermissionListView.as_view(), name="permission-list"),
    path(
        "permissions/<int:obj_id>/",
        views.PermissionDetailsView.as_view(),
        name="permission-detail",
    ),
    path(
        "permissions/search/",
        views.PermissionSearchView.as_view(),
        name="permission-search",
    ),
    path("staff-groups/", views.StaffGroupListView.as_view(), name="staff-group-list"),
    path(
        "staff-groups/<int:obj_id>/",
        views.StaffGroupDetailsView.as_view(),
        name="staff-group-detail",
    ),
    path(
        "staff-groups/search/",
        views.StaffGroupSearchView.as_view(),
        name="staff-group-search",
    ),
    path(
        "staff-departments/",
        views.StaffDepartmentListView.as_view(),
        name="staff-department-list",
    ),
    path(
        "staff-departments/<int:obj_id>/",
        views.StaffDepartmentDetailsView.as_view(),
        name="staff-department-detail",
    ),
    path(
        "staff-departments/search/",
        views.StaffDepartmentSearchView.as_view(),
        name="staff-department-search",
    ),
    path(
        "staff-courses/", views.StaffCourseListView.as_view(), name="staff-course-list"
    ),
    path(
        "staff-courses/<int:obj_id>/",
        views.StaffCourseDetailsView.as_view(),
        name="staff-course-detail",
    ),
    path(
        "staff-courses/search/",
        views.StaffCourseSearchView.as_view(),
        name="staff-course-search",
    ),
    path("staff-events/", views.StaffEventListView.as_view(), name="staff-event-list"),
    path(
        "staff-events/<int:obj_id>/",
        views.StaffEventDetailsView.as_view(),
        name="staff-event-detail",
    ),
    path(
        "staff-events/search/",
        views.StaffEventSearchView.as_view(),
        name="staff-event-search",
    ),
    path("staff-roles/", views.StaffRoleListView.as_view(), name="staff-role-list"),
    path(
        "staff-roles/<int:obj_id>/",
        views.StaffRoleDetailsView.as_view(),
        name="staff-role-detail",
    ),
    path(
        "staff-roles/search/",
        views.StaffRoleSearchView.as_view(),
        name="staff-role-search",
    ),
    path("group-roles/", views.GroupRoleListView.as_view(), name="group-role-list"),
    path(
        "group-roles/<int:obj_id>/",
        views.GroupRoleDetailsView.as_view(),
        name="group-role-detail",
    ),
    path(
        "group-roles/search/",
        views.GroupRoleSearchView.as_view(),
        name="group-role-search",
    ),
    path(
        "role-permissions/",
        views.RolePermissionListView.as_view(),
        name="role-permission-list",
    ),
    path(
        "role-permissions/<int:obj_id>/",
        views.RolePermissionDetailsView.as_view(),
        name="role-permission-detail",
    ),
    path(
        "role-permissions/search/",
        views.RolePermissionSearchView.as_view(),
        name="role-permission-search",
    ),
]
