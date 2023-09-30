# apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Attributes to include in list view
    list_display = [
        "username",
        "is_active",
    ]
    # Include additional custom attributes in Detail/Edit view
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Fields",
            {
                "fields": [
                    "active_dates",
                ]
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
