# apps/calendar/views.py

from datetime import date, datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.utils import timezone

from apps.calendar.models import ReadingDay
from apps.calendar.utils.coding_streak_helper import CodingStreak

from .models import CodingDay


def toggle_reading_day(request):
    if request.method == "POST":
        user = request.user
        if "date" in request.POST:
            # Parse the date from the POST data
            date_str = request.POST["date"]
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            # Use today's date if no date is provided
            date = timezone.now().date()

        try:
            reading_day = ReadingDay.objects.get(user=user, date=date)
            reading_day.delete()
        except ObjectDoesNotExist:
            ReadingDay.objects.create(user=user, date=date)

        return redirect("show_calendar", year=date.year, month=date.month)
    else:
        return HttpResponseBadRequest()


##########################################################
# Logic for coding streak calendar                       #
# (in isolation from user model and the rest of the app) #
##########################################################


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
