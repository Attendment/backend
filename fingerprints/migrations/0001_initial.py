# Generated by Django 4.1.1 on 2022-09-25 10:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fingerprint",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="fingerprints/", verbose_name="Template File"
                    ),
                ),
                (
                    "binary",
                    models.BinaryField(
                        blank=True, null=True, verbose_name="Fingerprint Data"
                    ),
                ),
            ],
        ),
    ]