from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]