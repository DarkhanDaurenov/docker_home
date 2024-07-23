from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from course.models import Course, CourseSubscription

User = get_user_model()

@shared_task
def send_course_update_notification(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = CourseSubscription.objects.filter(course=course)
    recipients = [sub.user.email for sub in subscriptions]

    send_mail(
        subject=f"Обновление курса: {course.title}",
        message=f"Курс '{course.title}' был обновлен. Проверьте новые материалы.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
    )


@shared_task
def check_inactive_users():
    month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=month_ago, is_active=True)

    inactive_users.update(is_active=False)

    print(f"Deactivated {inactive_users.count()} inactive users.")