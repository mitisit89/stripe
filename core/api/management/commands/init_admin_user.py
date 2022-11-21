from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from core.settings import (DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD,
                           DJANGO_SUPERUSER_USERNAME)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        username = DJANGO_SUPERUSER_USERNAME
        email = DJANGO_SUPERUSER_EMAIL
        password = DJANGO_SUPERUSER_PASSWORD
        if not User.objects.filter(username=username).exists():
            print("Creating account for %s (%s)" % (username, email))
            admin = User.objects.create_superuser(
                email=email, username=username, password=password
            )
        else:
            print("Admin account has already been initialized.")
