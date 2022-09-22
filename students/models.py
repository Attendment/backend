from django.db import models
from django.db.models.fields import uuid
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    class YearInSchool(models.TextChoices):
        LEVEL_100 = "100", "100"
        LEVEL_200 = "200", "200"
        LEVEL_300 = "300", "300"
        LEVEL_400 = "400", "400"

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    first_name = models.CharField(
        verbose_name=_("First Name"), max_length=50, null=False, blank=False
    )
    last_name = models.CharField(
        verbose_name=_("Last Name"), max_length=50, null=False, blank=False
    )
    other_names = models.CharField(
        verbose_name=_("Other Names"), max_length=100, null=False, blank=False
    )
    student_id = models.CharField(
        verbose_name=_("Student ID Number"), max_length=8, null=False, blank=False
    )
    index_number = models.CharField(
        verbose_name=_("Student Index Number"), max_length=8, null=False, blank=False
    )
    level = models.CharField(
        verbose_name=_("Level of Student"), max_length=3, choices=YearInSchool.choices
    )
    # registered_exams
    # fingerprint

    def get_full_name(self) -> str:
        """
        Return the full name of the student by combining the first name, other names and last name
        """
        if self.other_names:
            return f"{self.first_name} {self.other_names} {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()
