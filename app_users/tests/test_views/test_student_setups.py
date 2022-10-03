from django.urls import reverse
from faker import Faker
from model_bakery import baker
from rest_framework.test import APIClient, APITestCase

from app_users.models import *


class TestStudentSetup(APITestCase, APIClient):
    def setUp(self) -> None:
        self.fake = Faker()
        self.account = baker.make(Account)
        self.student_url = reverse("student-list")
        self.student = {
            "username": "test1234",
            "name": self.fake.name(),
            "dob": self.fake.date(),
            "gender": "Male",
            "secondary_email": self.fake.email(),
            "guardian_type": "other",
            "account": baker.make(Account).id,
        }
        self.update = {
            "username": "guruhein1234"
        }

        self.field_params = "WyJ1c2VybmFtZSIsICJuYW1lIl0="  # ["username", "name"]
        self.sort_params = "WyJnZW5kZXIiLCAiLWlkIl0="  # ["gender", "-id"]
        self.expand_params = "WyJhY2NvdW50Il0=" # ["account"]
        self.no_exist_params = "WyJ0ZXN0Il0=" # ["test"]
        self.invalid_params = "test"
        self.test_fields = ["username", "name"]
        self.test_expand = "account"
        self.reverse_id_sorts = "WyItaWQiXQ==" # ["-id"]
        self.filter_params = {
            "filter_params": [
                {"field_name": "id", "operator": "lt", "value": 4}
            ]
        }

        _students = [
            Student(
                username=self.fake.name() + "1234",
                name="aaa%s" % i,
                dob=self.fake.date(),
                gender="Male",
                secondary_email=self.fake.email(),
                guardian_type="other",
                account_id=baker.make(Account).id
            ) for i in range(5)
        ]

        Student.objects.bulk_create(_students)
        
        return super().setUp()
