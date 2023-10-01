"""
URL configuration for aapo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("apps.home.urls")),
    # dedicated endpoint namespace for `calendar` app with POC calendar implementation
    path("calendar/", include("apps.calendar.urls")),
    # django browser reload
    path("__reload__/", include("django_browser_reload.urls")),
]
