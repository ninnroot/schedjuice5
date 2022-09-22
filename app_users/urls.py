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
    path(
        "staff-bankaccounts/",
        views.StaffBankAccountListView.as_view(),
        name="staffbankaccounts-list",
    ),
    path(
        "staff-bankaccounts/search",
        views.StaffBankAccountSearchView.as_view(),
        name="staffbankaccounts-search",
    ),
    path(
        "staff-bankaccounts/<int:obj_id>",
        views.StaffBankAccountDetailsView.as_view(),
        name="staffbankaccounts-details",
    ),
    path(
        "staff-addresses/",
        views.StaffAddressListView.as_view(),
        name="staffaddresss-list",
    ),
    path(
        "staff-addresses/search",
        views.StaffAddressSearchView.as_view(),
        name="staffaddresss-search",
    ),
    path(
        "staff-addresses/<int:obj_id>",
        views.StaffAddressDetailsView.as_view(),
        name="staffaddresss-details",
    ),
    path(
        "student-bankaccounts/",
        views.StudentBankAccountListView.as_view(),
        name="staffbankaccounts-list",
    ),
    path(
        "student-bankaccounts/search",
        views.StudentBankAccountSearchView.as_view(),
        name="staffbankaccounts-search",
    ),
    path(
        "student-bankaccounts/<int:obj_id>",
        views.StudentBankAccountDetailsView.as_view(),
        name="staffbankaccounts-details",
    ),
    path(
        "student-addresses/",
        views.StudentAddressListView.as_view(),
        name="studentaddresss-list",
    ),
    path(
        "student-addresses/search",
        views.StudentAddressSearchView.as_view(),
        name="studentaddresss-search",
    ),
    path(
        "student-addresses/<int:obj_id>",
        views.StudentAddressDetailsView.as_view(),
        name="studentaddresss-details",
    ),
]
