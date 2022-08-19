from rest_framework import status
from model_bakery import baker
import pytest
from app_users.models import *
from .test_student_setups import TestStudentSetup

@pytest.mark.django_db
class TestCreateStudent(TestStudentSetup):

    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.post(self.student_url, self.student, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_data_is_valid_then_return_201(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(self.student_url, self.student, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_data_is_invalid_then_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response = self.client.post(self.student_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


@pytest.mark.django_db
class TestUpdateStudent(TestStudentSetup):
    
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        student = baker.make(Student)
        response = self.client.put(f"{self.student_url}/{student.id}", self.student, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_data_is_valid_then_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        student = baker.make(Student)
        print(student.id)
        response = self.client.put(f"{self.student_url}{student.id}", self.student, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_data_is_invalid_then_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        student = baker.make(Student)
        response = self.client.put(f"{self.student_url}{student.id}", {"username": "test"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 

    def test_if_student_does_not_exist_return_return_404(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.put(f"{self.student_url}999", self.student, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


@pytest.mark.django_db
class TestDeleteStudent(TestStudentSetup):

    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.delete(f"{self.student_url}/999")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_student_does_not_exist_return_return_404(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.delete(f"{self.student_url}999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_student_exist_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        student = baker.make(Student)
        response =self.client.delete(f"{self.student_url}{student.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


@pytest.mark.django_db
class TestListStudent(TestStudentSetup):

    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.get(self.student_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_student_exist_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.get(self.student_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_fields_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.get(f"{self.student_url}?fields={self.field_params}", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_fields_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.get(f"{self.student_url}?fields=test", format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_sort_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.get(f"{self.student_url}?sort={self.sort_params}", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_sort_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.get(f"{self.student_url}?sort=test", format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


@pytest.mark.django_db
class TestRetrieveStudent(TestStudentSetup):
    
    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.get(self.student_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_student_does_not_exist_return_return_404(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.get(f"{self.student_url}999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_student_exist_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        student = baker.make(Student)
        response =self.client.get(f"{self.student_url}{student.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


@pytest.mark.django_db
class TestSearchStudent(TestStudentSetup):

    @pytest.mark.skip(reason="not implemented")
    def test_if_user_is_anynomous_then_return_401(self):
        response = self.client.post(f"{self.student_url}search", self.filter_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_filter_params_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.post(f"{self.student_url}search", self.filter_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_filter_params_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.post(f"{self.student_url}search", {"filter_params": "test"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_fields_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.post(f"{self.student_url}search?fields={self.field_params}", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_fields_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.post(f"{self.student_url}search?fields=test", format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_sort_is_valid_return_200(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.post(f"{self.student_url}search?sort={self.sort_params}", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_sort_is_invalid_return_400(self):
        # self.force_authenticate(user=Account(is_student=True))
        response =self.client.post(f"{self.student_url}search?sort=test", format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



