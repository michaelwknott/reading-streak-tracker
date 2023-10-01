# apps/calendar/templatetags/custom_calendar_tags.py
import calendar
from typing import NamedTuple

from django import template

register = template.Library()


class Day(NamedTuple):
    day: int
    read: bool


@register.inclusion_tag("calendar/_reading_streak.html")
def insert_reading_streak(user, year, month):
    current_user_reading_days = user.get_reading_days(year, month)
    cal = calendar.monthcalendar(year, month)
    streak_calendar = []
    for week in cal:
        this_week = []
        for day in week:
            read = day in current_user_reading_days
            this_week.append(Day(day, read))
        streak_calendar.append(this_week)

    month_name = calendar.month_name[month]
    return {"streak_calendar": streak_calendar, "month_name": month_name, "year": year}
