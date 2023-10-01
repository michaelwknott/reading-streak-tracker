# apps/home/views.py
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    return render(request, "home/index.html")


@login_required
def calendar(request):
    # redirect to calendar for current year and month
    today = datetime.today()
    return redirect("show_calendar", year=today.year, month=today.month)


@login_required
def show_calendar(request, year, month):
    year, month = int(year), int(month)  # passed via POST request in form, ensure they are integers
    return render(request, "home/calendar.html", {"year": year, "month": month})


def test(request):
    return render(request, "home/test.html")
