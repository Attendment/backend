# Generated by Django 4.1.1 on 2022-09-22 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_course_programme_room_student_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="programme_of_study",
            field=models.ForeignKey(
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students",
                related_query_name="student",
                to="students.programme",
            ),
        ),
    ]
