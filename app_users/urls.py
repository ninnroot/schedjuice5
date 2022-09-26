from django.urls import path

from . import views

urlpatterns = [
    path("addresses/", views.AddressListView.as_view(), name="address-list"),
    path("addresses/search", views.AddressSearchView.as_view(), name="address-search"),
    path(
        "addresses/<int:obj_id>",
        views.AddressDetailsView.as_view(),
        name="address-details",
    ),
    path(
        "phone_numbers/", views.PhoneNumberListView.as_view(), name="phone-number-list"
    ),
    path(
        "phone_numbers/search",
        views.PhoneNumberSearchView.as_view(),
        name="phone-number-search",
    ),
    path(
        "phone_numbers/<int:obj_id>",
        views.PhoneNumberDetailsView.as_view(),
        name="phone-number-details",
    ),
    path("bankaccounts/", views.BankAccountListView.as_view(), name="bankaccount-list"),
    path(
        "bankaccounts/search",
        views.BankAccountSearchView.as_view(),
        name="bankaccount-search",
    ),
    path(
        "bankaccounts/<int:obj_id>",
        views.BankAccountDetailsView.as_view(),
        name="bankaccount-details",
    ),
    path("staffs/", views.StaffListView.as_view(), name="staff-list"),
    path("staffs/search", views.StaffSearchView.as_view(), name="staff-search"),
    path("staffs/<int:obj_id>", views.StaffDetailsView.as_view(), name="staff-details"),
    path("guardians/", views.GuardianListView.as_view(), name="guardian-list"),
    path(
        "guardians/search", views.GuardianSearchView.as_view(), name="guardian-search"
    ),
    path(
        "guardians/<int:obj_id>",
        views.GuardianDetailsView.as_view(),
        name="guardian-details",
    ),
    path("students/", views.StudentListView.as_view(), name="student-list"),
    path("students/search", views.StudentSearchView.as_view(), name="student-search"),
    path(
        "students/<int:obj_id>",
        views.StudentDetailsView.as_view(),
        name="student-details",
    ),
]
