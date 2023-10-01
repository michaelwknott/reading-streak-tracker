# db.py
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CodingDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, unique=True)

    @classmethod
    def get_coding_days(cls, year, month):
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)
        return [
            day.date.day
            for day in cls.query.filter(cls.date >= start_date, cls.date < end_date).all()
        ]
