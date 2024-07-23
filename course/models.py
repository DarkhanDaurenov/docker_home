from django.db import models
from django.utils import timezone


class Course(models.Model):
    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    photo = models.ImageField(
        upload_to="images/course",
        blank=True,
        null=True,
        verbose_name="Картинку",
        help_text="Загрузите картинку",
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Опишите курс"
    )
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name="владелец", help_text="Укажите владельца курса")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Последнее обновление")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="Опишите урок"
    )
    photo = models.ImageField(
        upload_to="images/course",
        blank=True,
        null=True,
        verbose_name="Картинку",
        help_text="Загрузите картинку",
    )
    video_url = models.URLField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
    )
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, null=True, related_name="уроки"
    )
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True,  verbose_name="владелец", help_text="Укажите владельца")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class CourseSubscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)


    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user} подписан на {self.course}"
