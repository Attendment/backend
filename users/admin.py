# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "username",
        "email",
        "date_joined",
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "invigilator",
    )
    list_filter = (
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "invigilator",
    )
    raw_id_fields = ("groups", "user_permissions")
    readonly_fields = ("password", "date_joined", "last_login")
