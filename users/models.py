from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    invigilator = models.BooleanField(
        verbose_name=_("Invigilator"),
        help_text="Is this user an invigilator?",
        default=False,  # type: ignore
    )
    # lecturer id
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def __str__(self):
        return f"{self.get_full_name()}"
