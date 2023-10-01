# apps/calendar/models.py
from django.db import models
from apps.users.models import CustomUser


class ReadingDay(models.Model):
    date = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "date"),)

    def __str__(self):
        return f"<ReadingDay {self.date} for {self.user.username}>"


class CodingDay(models.Model):
    date = models.DateField(unique=True)

    @classmethod
    def get_coding_days(cls, year, month):
        """
        This builds a list representation of the active days (as stored in this ORM model),
        for a given month.
        """
        from datetime import datetime

        # Determine relevant date range to check activity for
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)

        # Return list of active days
        return [day.date.day for day in cls.objects.filter(date__range=(start_date, end_date))]

    def __str__(self):
        return f"<CodingDay {self.date}>"
