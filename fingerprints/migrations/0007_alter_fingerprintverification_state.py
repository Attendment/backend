# Generated by Django 4.1.1 on 2022-09-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fingerprints", "0006_fingerprintverification"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fingerprintverification",
            name="state",
            field=models.BooleanField(verbose_name="state"),
        ),
    ]