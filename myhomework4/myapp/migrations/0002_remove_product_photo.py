from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="photo",
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]