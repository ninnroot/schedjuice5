import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_staff(api_client):
    def get_staff(staff):
        return api_client.post("/api/v2/staffs/", staff)

    return get_staff
