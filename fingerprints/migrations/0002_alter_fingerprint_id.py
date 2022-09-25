# Generated by Django 4.1.1 on 2022-09-25 22:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("fingerprints", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fingerprint",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
