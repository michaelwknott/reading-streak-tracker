# apps/home/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "calendar/", views.calendar, name="calendar"
    ),  # redirects to calendar for current year and month
    path("calendar/<int:year>/<int:month>/", views.show_calendar, name="show_calendar"),
    path("test/", views.test, name="test"),
]
