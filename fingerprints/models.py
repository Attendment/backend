import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Fingerprint(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        blank=False,
        null=False,
        editable=False,
    )
    created = models.DateTimeField(
        verbose_name=_("Created"),
        null=False,
        blank=False,
        auto_now_add=True,
    )
    file = models.FileField(
        verbose_name=_("Template File"),
        upload_to="fingerprints/",
        blank=False,
        null=False,
    )
    binary = models.BinaryField(
        verbose_name=_("Fingerprint Data"), null=True, blank=True
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.id}"
