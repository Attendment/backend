# Generated by Django 4.1.1 on 2022-09-26 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fingerprints", "0002_fingerprint_student"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fingerprint",
            name="student",
        ),
    ]
