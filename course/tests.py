from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from course.models import Course, Lesson, CourseSubscription


class CourseAndLessonTests(APITestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass')
        self.moder = User.objects.create_user(email='moderator@example.com', password='testpass', is_staff=True)
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(title="Test Course", description="Test Description", owner=self.user)
        self.lesson = Lesson.objects.create(title="Test Lesson", video_url="http://youtube.com", course=self.course, owner=self.user)

    def test_create_lesson(self):
        url = reverse('course:lesson_create')
        data = {'title': 'New Lesson', 'video_url': 'http://youtube.com', 'course': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_lesson(self):
        url = reverse('course:lesson_update', kwargs={'pk': self.lesson.id})
        data = {'title': 'Updated Lesson'}
        self.client.force_authenticate(user=self.moder)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'Updated Lesson')

    def test_delete_lesson(self):
        url = reverse('course:lesson_destroy', kwargs={'pk': self.lesson.id})
        self.client.force_authenticate(user=self.moder)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_subscribe_to_course(self):
        url = reverse('course:course_subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        CourseSubscription.objects.create(user=self.user, course=self.course)
        url = reverse('course:course_subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())