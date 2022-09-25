# Generated by Django 4.1.1 on 2022-09-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0010_delete_course"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exam",
            name="students",
        ),
        migrations.AddField(
            model_name="student",
            name="registered_exams",
            field=models.ManyToManyField(
                related_name="students",
                related_query_name="student",
                to="students.exam",
            ),
        ),
    ]