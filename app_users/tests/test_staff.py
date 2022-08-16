from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APITestCase
from rest_framework import status
from model_bakery import baker
from faker import Faker
import pytest
from app_users.models import *

@pytest.mark.django_db
class TestCreateStaff:

    fake = Faker()

    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self, create_staff):
        account = baker.make(Account)
        response = create_staff({
                    "username": "test1test1",
                    "name": "test",
                    "dob": "2021-10-04",
                    "gender": "Male",
                    "secondary_email": "test@gmail.com",
                    "primary_phone_number": "0912313123",
                    "secondary_phone_number": "09123213123",
                    "account": account.id
                })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_valid_then_return_201(self, create_staff):
        account = baker.make(Account)
        img = SimpleUploadedFile("images/test-profile.png", b"file_content", content_type="image/png")
        response = create_staff({
                    "username": "test1test1",
                    "name": "test",
                    "dob": "2021-10-04",
                    "gender": "Male",
                    "secondary_email": "test@gmail.com",
                    "primary_phone_number": "0912313123",
                    "secondary_phone_number": "09123213123",
                    "account": account.id
                })
        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_then_return_400(self, create_staff):
        account = baker.make(Account)
        response = create_staff({
                        "username": "",
                        "name": "",
                        "dob": "",
                        "gender": "",
                        "secondary_email": "",
                        "primary_phone_number": "",
                        "secondary_phone_number": "",
                        "account": account.id
                    })
        print("errors", response.data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    