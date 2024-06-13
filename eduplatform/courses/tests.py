from datetime import timedelta, datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Course, Group
from users.models import CustomUser, Teacher, Student


class BaseTestSetup(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Programming",
            description="Learn Python programming language",
            duration=timedelta(days=30)
        )
        self.student1 = Student.objects.create(
            rating=85,
            user=CustomUser.objects.create(email="student1@example.com", first_name="John", last_name="Doe")
        )
        self.student2 = Student.objects.create(
            rating=70,
            user=CustomUser.objects.create(email="student2@example.com", first_name="Jane", last_name="Smith")
        )
        self.teacher = Teacher.objects.create(
            user=CustomUser.objects.create(email="teacher@example.com", first_name="Mike", last_name="Johnson")
        )

        self.group = Group.objects.create(
            title='test',
            date_formation='2000-01-01',
            course=self.course,
            teacher=self.teacher
        )
        self.group.students.set([self.student1, self.student2])


class CreateGroupTest(BaseTestSetup):

    def test_create_group(self):
        url = reverse('group-list')
        data = {
            'title': 'test',
            'date_formation': '2000-01-01',
            'course': self.course.pk,
            'students': [self.student1.pk, self.student2.pk],
            'teacher': self.teacher.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateGroupTest(BaseTestSetup):

    def test_update_group(self):
        url = reverse('group-detail', kwargs={'pk': self.group.pk})
        data = {
            'title': 'new test',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteGroupTest(BaseTestSetup):

    def test_delete_group(self):
        url = reverse('group-detail', kwargs={'pk': self.group.pk})
        time_before = datetime.now()
        response = self.client.delete(url, format='json')
        time_after = datetime.now()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertLess(time_before, time_after)


class ReadGroupTest(BaseTestSetup):

    def test_read_group_list(self):
        url = reverse('group-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_group_detail(self):
        url = reverse('group-detail', kwargs={'pk': self.group.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
