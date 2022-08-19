from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from model_bakery import baker
from faker import Faker

from app_users.models import *

class TestStudentSetup(APITestCase, APIClient):

    def setUp(self) -> None:
        self.fake = Faker()
        self.account = baker.make(Account)
        self.phone_number = baker.make(PhoneNumber)
        self.student_url = reverse('student-list')
        self.student = {
            "username": "test1234",
            "name": self.fake.name(),
            "dob": self.fake.date(),
            "gender": "Male",
            "secondary_email": self.fake.email(),
            "phone_number": self.phone_number.id,
            "guardian_type": "other",
            "account": self.account.id
        }
        self.field_params = "WyJ1c2VybmFtZSIsICJuYW1lIl0=" #["username", "name"]
        self.sort_params = "WyJnZW5kZXIiLCAiLWlkIl0=" #["gender", "-id"]
        self.filter_params = {
                                "filter_params": [
                                    {
                                        "field_name": "id",
                                        "operator": "lt",
                                        "value": 4
                                    },
                                    {
                                        "field_name": "name",
                                        "operator": "icontains",
                                        "value": "a"
                                    }
                                ]
                            }
        return super().setUp()