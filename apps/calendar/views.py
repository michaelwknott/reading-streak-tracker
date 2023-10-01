# apps/calendar/views.py

from datetime import date
from .models import CodingDay
from apps.calendar.utils.coding_streak_helper import CodingStreak

from django.shortcuts import render, redirect
from datetime import datetime, date
from .models import CodingDay
from .script import CodingStreak

def calendar_in_isolation(request):
    today = date.today()
    return redirect("show_calendar_in_isolation", year=today.year, month=today.month)


def show_calendar_in_isolation(request, year, month):
    coding_days = CodingDay.get_coding_days(year, month)
    cs = CodingStreak(year, month, coding_days)
    html_calendar = cs.create_streak_calendar_as_html()

    return render(request, "calendar/calendar_in_isolation.html", {"html_calendar": html_calendar})


def toggle_coding_day_today(request):
    if request.method == "POST":
        today = date.today()
        toggle_coding_day(today)
        return redirect("show_calendar_in_isolation", year=today.year, month=today.month)


def toggle_coding_day_by_form(request):
    if request.method == "POST":
        date_str = request.POST.get("date")
        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            toggle_coding_day(date_obj)
            return redirect("show_calendar_in_isolation", year=date_obj.year, month=date_obj.month)
        else:
            # No date was provided, so do nothing and redirect to today's calendar
            # This should not happen since client-side validation is in place
            today = date.today()
            return redirect("show_calendar_in_isolation", year=today.year, month=today.month)


def toggle_coding_day(target_date):
    try:
        coding_day = CodingDay.objects.get(date=target_date)
        coding_day.delete()
    except CodingDay.DoesNotExist:
        CodingDay.objects.create(date=target_date)
