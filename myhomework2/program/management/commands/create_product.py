from django.core.management.base import BaseCommand
from program.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Tea',
                       description='Fire Toa',
                       price=250.00,
                       quantity=10)
        product.save()
        self.stdout.write(f'{product}')