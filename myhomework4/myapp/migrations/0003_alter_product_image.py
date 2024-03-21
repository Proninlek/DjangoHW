from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_remove_product_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]