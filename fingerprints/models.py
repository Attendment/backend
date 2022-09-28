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
    fingerprint_id = models.CharField(
        verbose_name=_("Fingerprint ID"), null=True, blank=True, max_length=100
    )

    def __str__(self):
        return f"{self.fingerprint_id}"

    class Meta:
        ordering = ("-created",)
