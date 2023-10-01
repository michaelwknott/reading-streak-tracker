# apps/calendar/admin.py
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import CodingDay, ReadingDay


@admin.register(CodingDay)
class CustomCodingDay(ModelAdmin):
    model = CodingDay
    # Attributes to include in list view
    list_display = [
        "date",
    ]


@admin.register(ReadingDay)
class CustomReadingDay(ModelAdmin):
    model = ReadingDay
    # Attributes to include in list view
    list_display = [
        "date",
        "user",
    ]
