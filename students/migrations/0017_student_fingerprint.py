# Generated by Django 4.1.1 on 2022-09-25 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fingerprints", "0001_initial"),
        ("students", "0016_student_registered_exams"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="fingerprint",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="fingerprints.fingerprint",
                verbose_name="Fingerprint",
            ),
        ),
    ]