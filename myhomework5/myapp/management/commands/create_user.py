from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Mike', email='mike@example.com', password='secrete', age=25)
        user.save()
        self.stdout.write(f'{user}')