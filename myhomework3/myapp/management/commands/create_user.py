from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Ivanko', email='vano@mail.by', password='123456789', age=40)
        user.save()
        self.stdout.write(f'{user}')