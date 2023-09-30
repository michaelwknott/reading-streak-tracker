# apps/home/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


# @login_required
def calendar(request):
    return render(request, "home/calendar.html")
