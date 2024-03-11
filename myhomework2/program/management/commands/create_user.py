from django.core.management.base import BaseCommand
from program.models import User

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Василий',
                    age=38,
                    email='mail@example.com',
                    phone='12345678',
                    address='Какой-то',
                    password='12345678')
        user.save()
        self.stdout.write(f'{user}')