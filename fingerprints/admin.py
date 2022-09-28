# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Fingerprint


@admin.register(Fingerprint)
class FingerprintAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "fingerprint_id")
    list_filter = ("created",)
