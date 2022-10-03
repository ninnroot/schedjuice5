from turtle import back
import pytest
from model_bakery import baker
from rest_framework import status

from app_users.models import *

from .test_student_setups import TestStudentSetup


@pytest.mark.django_db
class TestCreateStudent(TestStudentSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.post(self.student_url, self.student, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_data_is_valid_then_return_201(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(self.student_url, self.student, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_data_is_invalid_then_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(self.student_url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


@pytest.mark.django_db
class TestUpdateStudent(TestStudentSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.put(
            f"{self.student_url}1", self.student, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_data_is_valid_then_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        student = baker.make(Student)
        response = self.client.put(
            f"{self.student_url}{student.id}", self.update, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("guruhein1234", response.json()['data']['username'])

    def test_if_data_is_invalid_then_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        student = baker.make(Student)
        response = self.client.put(
            f"{self.student_url}{student.id}", {"username": "test"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_student_does_not_exist_return_return_404(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.put(
            f"{self.student_url}999", self.student, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


@pytest.mark.django_db
class TestDeleteStudent(TestStudentSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.delete(f"{self.student_url}/999")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_student_does_not_exist_return_return_404(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.delete(f"{self.student_url}999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_student_exist_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        student = baker.make(Student)
        response = self.client.delete(f"{self.student_url}{student.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


@pytest.mark.django_db
class TestListStudent(TestStudentSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.get(self.student_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_student_exist_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.get(self.student_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])

    def test_if_fields_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.get(
            f"{self.student_url}?fields={self.field_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(self.test_fields, list(response.json()['data'][0].keys()))

    def test_if_fields_not_in_models_return_empty(self):
        response = self.client.get(
            f"{self.student_url}?fields={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(bool(response.data['data'][0]))

    def test_if_fields_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.get(f"{self.student_url}?fields={self.invalid_params}", format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_sorts_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.get(
            f"{self.student_url}?sorts={self.sort_params}", format="json"
        )
        students_id = [student["id"] for student in response.json()['data']]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(sorted(students_id)[::-1], students_id)

    def test_if_sorts_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.get(f"{self.student_url}?sorts={self.invalid_params}", format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_sorts_not_in_models_return_400(self):
        response = self.client.get(
            f"{self.student_url}?sorts={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_expand_is_valid_return_200(self):
        response = self.client.get(
            f"{self.student_url}?expand={self.expand_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.test_expand, response.json()["data"][0])

    def test_if_expand_not_in_models_return_200(self):
        response = self.client.get(
            f"{self.student_url}?expand={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_expand_is_invalid_return_400(self):
        response = self.client.get(
            f"{self.student_url}?expand={self.invalid_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


@pytest.mark.django_db
class TestRetrieveStudent(TestStudentSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.get(self.student_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_student_does_not_exist_return_return_404(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.get(f"{self.student_url}999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_student_exist_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        student = baker.make(Student)
        response = self.client.get(f"{self.student_url}{student.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])

    def test_if_fields_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_staff=True))
        student = baker.make(Student)
        response = self.client.get(
            f"{self.student_url}{student.id}?fields={self.field_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(self.test_fields, list(response.json()['data'].keys()))

    def test_if_fields_not_in_models_return_empty(self):
        student = baker.make(Student)
        response = self.client.get(
            f"{self.student_url}{student.id}?fields={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(bool(response.data['data']))

    def test_if_fields_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_staff=True))
        student = baker.make(Student)
        response = self.client.get(f"{self.student_url}{student.id}?fields={self.invalid_params}", format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_expand_is_valid_return_200(self):
        student = baker.make(Student)
        response = self.client.get(
            f"{self.student_url}{student.id}?expand={self.expand_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.test_expand, response.json()["data"])

    def test_if_expand_not_in_models_return_200(self):
        student = baker.make(Student)
        response = self.client.get(
            f"{self.student_url}{student.id}?expand={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_expand_is_invalid_return_400(self):
        student = baker.make(Student)
        response = self.client.get(
            f"{self.student_url}{student.id}?expand={self.invalid_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


@pytest.mark.django_db
class TestSearchStudent(TestStudentSetup):
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.post(
            f"{self.student_url}search", self.filter_params, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_filter_params_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(
            f"{self.student_url}search", self.filter_params, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertNotEqual(response.data['data'], [])

    def test_if_filter_params_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(
            f"{self.student_url}search", {"filter_params": "test"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_fields_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(
            f"{self.student_url}search?fields={self.field_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(self.test_fields, list(response.json()['data'][0].keys()))

    def test_if_fields_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(
            f"{self.student_url}search?fields={self.invalid_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_fields_not_in_models_return_empty(self):
        response = self.client.post(
            f"{self.student_url}search?fields={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(bool(response.data['data'][0]))

    def test_if_sorts_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(
            f"{self.student_url}search?sorts={self.sort_params}", format="json"
        )
        students_id = [student["id"] for student in response.json()['data']]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['data'], [])
        self.assertListEqual(sorted(students_id)[::-1], students_id)

    def test_if_sorts_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(
            f"{self.student_url}search?sorts={self.invalid_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_sorts_not_in_models_return_400(self):
        response = self.client.post(
            f"{self.student_url}search?sorts={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_expand_is_valid_return_200(self):
        response = self.client.post(
            f"{self.student_url}search?expand={self.expand_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.test_expand, response.json()["data"][0])

    def test_if_expand_not_in_models_return_200(self):
        response = self.client.post(
            f"{self.student_url}search?expand={self.no_exist_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_expand_is_invalid_return_400(self):
        response = self.client.post(
            f"{self.student_url}search?expand={self.invalid_params}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
