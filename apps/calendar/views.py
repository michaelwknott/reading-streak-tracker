# apps/calendar/views.py

from django.shortcuts import render, redirect
from datetime import datetime, date
from .models import CodingDay
from .script import CodingStreak


def show_calendar(request, year, month):
    coding_days = CodingDay.get_coding_days(year, month)

    # NEXT:Look at this part more closely and refactor
    ### START ###
    cs = CodingStreak(year, month, coding_days)
    html_calendar = cs.create_streak_calendar_as_html()
    ### END ###

    return render(request, "calendar/calendar.html", {"html_calendar": html_calendar})


def toggle_coding_day_today(request):
    if request.method == "POST":
        today = date.today()
        toggle_coding_day(today)
        return redirect("show_calendar", year=today.year, month=today.month)


def toggle_coding_day_by_form(request):
    if request.method == "POST":
        date_str = request.POST.get("date")
        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            toggle_coding_day(date_obj)
            return redirect("show_calendar", year=date_obj.year, month=date_obj.month)
        else:
            # No date was provided, so do nothing and redirect to today's calendar
            # This should not happen since client-side validation is in place
            today = date.today()
            return redirect("show_calendar", year=today.year, month=today.month)


def toggle_coding_day(target_date):
    try:
        coding_day = CodingDay.objects.get(date=target_date)
        coding_day.delete()
    except CodingDay.DoesNotExist:
        CodingDay.objects.create(date=target_date)
