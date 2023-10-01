# apps/users/models.py

from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Note: e-mail, first_name, last_name, password and username are inherited from AbstractUser
    active_dates = models.JSONField(
        default=list, help_text="Dates stored as ISO formatted strings in a list"
    )

    def get_reading_days(self, year, month):
        """
        This builds a list representation of the active days (as stored in this ORM model),
        for a given month.
        """
        from datetime import datetime

        start_date = datetime(year, month, 1)
        end_date = datetime(year, month + 1, 1) if month != 12 else datetime(year + 1, 1, 1)
        return [
            day.date.day for day in self.readingday_set.filter(date__range=(start_date, end_date))
        ]

    def add_active_date(self, date: datetime.date) -> None:
        """
        Add a new active date to the active_dates JSON field.
        Also ensures no duplicate dates are added.
        (JSON field doesn't natively support a set data type.)

        Args:
            date (datetime.date): The date to be added.
        """
        date_str = date.isoformat()
        if date_str not in self.active_dates:
            self.active_dates.append(date_str)
            self.active_dates.sort()  # keep dates sorted for convenience
            self.save()

    def get_active_dates(self) -> list[datetime.date]:
        """
        Retrieve the active dates as datetime.date objects.

        Returns:
            list: A list of datetime.date objects representing the active dates.
        """
        return [datetime.fromisoformat(date) for date in self.active_dates]

    def __str__(self):
        return self.username
