import pytest
from model_bakery import baker
from rest_framework import status

from app_users.models import *

from .test_staff_setups import TestStaffSetup


@pytest.mark.django_db
class TestCreateStaff(TestStaffSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.post(self.staff_url, self.staff, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_data_is_valid_then_return_201(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.post(self.staff_url, self.staff, format="json")
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_data_is_invalid_then_return_400(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.post(self.staff_url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


@pytest.mark.django_db
class TestUpdateStaff(TestStaffSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.put(
            f"{self.staff_url}1", self.staff, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_data_is_valid_then_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        staff = baker.make(Staff)
        response = self.client.put(
            f"{self.staff_url}{staff.id}", self.update, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("guruhein1234", response.json()['data']['username'])

    def test_if_data_is_invalid_then_return_400(self):
        # self.force_authenticate(user=Account(is_staff=True))
        staff = baker.make(Staff)
        response = self.client.put(
            f"{self.staff_url}{staff.id}", {"username": "test"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_staff_does_not_exist_return_return_404(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.put(f"{self.staff_url}999", self.staff, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


@pytest.mark.django_db
class TestDeleteStaff(TestStaffSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.delete(f"{self.staff_url}/999")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_staff_does_not_exist_return_404(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.delete(f"{self.staff_url}999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_staff_exist_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        staff = baker.make(Staff)
        response = self.client.delete(f"{self.staff_url}{staff.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


@pytest.mark.django_db
class TestListStaff(TestStaffSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.get(self.staff_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_staff_exist_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.get(self.staff_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])

    def test_if_fields_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.get(
            f"{self.staff_url}?fields={self.field_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(self.test_fields, list(response.json()['data'][0].keys()))

    def test_if_fields_not_in_models_return_empty(self):
        response = self.client.get(
            f"{self.staff_url}?fields={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(bool(response.data['data'][0]))

    def test_if_fields_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.get(f"{self.staff_url}?fields={self.invalid_params}", format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_sorts_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.get(
            f"{self.staff_url}?sorts={self.reverse_id_sorts}", format="json"
        )
        staffs_id = [staff["id"] for staff in response.json()['data']]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(sorted(staffs_id)[::-1], staffs_id)

    def test_if_sorts_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.get(f"{self.staff_url}?sorts={self.invalid_params}", format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_sorts_not_in_models_return_400(self):
        response = self.client.get(
            f"{self.staff_url}?sorts={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_expand_is_valid_return_200(self):
        response = self.client.get(
            f"{self.staff_url}?expand={self.expand_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.test_expand, response.json()["data"][0])

    def test_if_expand_not_in_models_return_200(self):
        response = self.client.get(
            f"{self.staff_url}?expand={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_expand_is_invalid_return_400(self):
        response = self.client.get(
            f"{self.staff_url}?expand={self.invalid_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


@pytest.mark.django_db
class TestRetrieveStaff(TestStaffSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.get(self.staff_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_staff_does_not_exist_return_return_404(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.get(f"{self.staff_url}999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_staff_exist_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        staff = baker.make(Staff)
        response = self.client.get(f"{self.staff_url}{staff.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])

    def test_if_fields_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        staff = baker.make(Staff)
        response = self.client.get(
            f"{self.staff_url}{staff.id}?fields={self.field_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(self.test_fields, list(response.json()['data'].keys()))

    def test_if_fields_not_in_models_return_empty(self):
        staff = baker.make(Staff)
        response = self.client.get(
            f"{self.staff_url}{staff.id}?fields={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(bool(response.data['data']))

    def test_if_fields_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_staff=True))
        staff = baker.make(Staff)
        response = self.client.get(f"{self.staff_url}{staff.id}?fields={self.invalid_params}", format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_expand_is_valid_return_200(self):
        staff = baker.make(Staff)
        response = self.client.get(
            f"{self.staff_url}{staff.id}?expand={self.expand_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.test_expand, response.json()["data"])

    def test_if_expand_not_in_models_return_200(self):
        staff = baker.make(Staff)
        response = self.client.get(
            f"{self.staff_url}{staff.id}?expand={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_expand_is_invalid_return_400(self):
        staff = baker.make(Staff)
        response = self.client.get(
            f"{self.staff_url}{staff.id}?expand={self.invalid_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


@pytest.mark.django_db
class TestSearchStaff(TestStaffSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.post(
            f"{self.staff_url}search", self.filter_params, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_filter_params_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.post(
            f"{self.staff_url}search", self.filter_params, format="json"
        )
        print(response.data["data"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertNotEqual(response.data['data'], [])

    def test_if_filter_params_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.post(
            f"{self.staff_url}search", {"filter_params": "test"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_fields_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.post(
            f"{self.staff_url}search?fields={self.field_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(self.test_fields, list(response.json()['data'][0].keys()))

    def test_if_fields_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.post(
            f"{self.staff_url}search?fields={self.invalid_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_fields_not_in_models_return_empty(self):
        response = self.client.post(
            f"{self.staff_url}search?fields={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(bool(response.data['data'][0]))

    def test_if_sorts_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.post(
            f"{self.staff_url}search?sorts={self.sort_params}", format="json"
        )
        staffs_id = [staff["id"] for staff in response.json()['data']]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(sorted(staffs_id)[::-1], staffs_id)

    def test_if_sorts_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_staff=True))
        response = self.client.post(f"{self.staff_url}search?sorts={self.invalid_params}", format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_sorts_not_in_models_return_400(self):
        response = self.client.post(
            f"{self.staff_url}search?sorts={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_expand_is_valid_return_200(self):
        response = self.client.post(
            f"{self.staff_url}search?expand={self.expand_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.test_expand, response.json()["data"][0])

    def test_if_expand_not_in_models_return_200(self):
        response = self.client.post(
            f"{self.staff_url}search?expand={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_expand_is_invalid_return_400(self):
        response = self.client.post(
            f"{self.staff_url}search?expand={self.invalid_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
