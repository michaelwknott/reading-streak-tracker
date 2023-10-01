# apps/calendar/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("<int:year>/<int:month>/", views.show_calendar, name="show_calendar"),
    path("add_coding_day/", views.toggle_coding_day_today, name="toggle_coding_day_today"),
    path(
        "add_today_coding_day/", views.toggle_coding_day_by_form, name="toggle_coding_day_by_form"
    ),
]
