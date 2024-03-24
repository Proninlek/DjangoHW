from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        prod = Product(name='Beer', price=120.0, description='light')
        prod.save()
        self.stdout.write(f'{prod}')