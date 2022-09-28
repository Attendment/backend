# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Fingerprint


@admin.register(Fingerprint)
class FingerprintAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'file', 'binary')
    list_filter = ('created',)
