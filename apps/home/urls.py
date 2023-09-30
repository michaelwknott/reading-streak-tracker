# apps/home/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("calendar/", views.calendar, name="calendar"),
]
