from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_order_date_ordered"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_ordered",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]