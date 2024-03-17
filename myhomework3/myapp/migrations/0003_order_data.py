import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_order_total_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_ordered",
            field=models.DateTimeField(verbose_name=datetime.datetime.today),
        ),
    ]