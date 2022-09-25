# Generated by Django 4.1.1 on 2022-09-25 11:44

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A lecturer with that ID already exists."},
                max_length=10,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="Lecturer ID",
            ),
        ),
    ]
