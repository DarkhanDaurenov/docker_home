from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="takishev89@yandex.kz")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("87006856130")
        user.save()