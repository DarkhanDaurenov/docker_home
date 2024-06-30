from django.urls import path
from rest_framework.routers import SimpleRouter

from course.apps import CourseConfig
from course.views import (CourseViewSet, LessonCreateAPIView,
                          LessonDestroyAPIView, LessonListAPIView,
                          LessonRetrieveAPIView, LessonUpdateAPIView)

app_name = CourseConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path(
        "lesson/<int:pk>/destroy/",
        LessonDestroyAPIView.as_view(),
        name="lesson_destroy",
    ),
    path(
        "lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
]

urlpatterns += router.urls
