# apps/calendar/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("toggle_reading_day/", views.toggle_reading_day, name="toggle_reading_day"),
    # Paths for initial POC of calendar (isolated from user model and the rest of the app)
    path(
        "calendar_in_isolation/", views.calendar_in_isolation, name="calendar_in_isolation"
    ),  # redirects to calendar for current year and month
    path(
        "calendar_in_isolation/<int:year>/<int:month>/",
        views.show_calendar_in_isolation,
        name="show_calendar_in_isolation",
    ),
    path("add_coding_day/", views.toggle_coding_day_today, name="toggle_coding_day_today"),
    path(
        "add_today_coding_day/", views.toggle_coding_day_by_form, name="toggle_coding_day_by_form"
    ),
]
