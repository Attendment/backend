# Generated by Django 4.1.1 on 2022-09-23 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0009_remove_exam_course_exam_course_code_exam_course_name"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Course",
        ),
    ]