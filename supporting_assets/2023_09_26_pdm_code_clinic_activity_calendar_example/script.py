# script.py
import calendar
from typing import NamedTuple


class Day(NamedTuple):
    day: int
    coded: bool


class CodingStreak:
    def __init__(self, year: int, month: int, coding_days: list[int]):
        self.year = year
        self.month = month
        self.coding_days = coding_days
        self.cal = calendar.monthcalendar(self.year, self.month)
        self.streak_calendar = self._create_streak_calendar()

    def _create_streak_calendar(self):
        streak_calendar = []
        for week in self.cal:
            this_week = []
            for day in week:
                coded = int(day) in self.coding_days
                this_week.append(Day(day, coded))
            streak_calendar.append(this_week)
        return streak_calendar

    def create_streak_calendar_as_html(self) -> str:
        month_name = calendar.month_name[self.month]
        output = []
        output.append("<table>")
        output.append(f"<tr>{month_name} {self.year}</tr>")
        output.append("<tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th>")
        output.append("<th>Fri</th><th>Sat</th><th>Sun</th></tr>")
        for week in self.streak_calendar:
            output.append("<tr>")
            for day in week:
                if day.day == 0:
                    output.append("<td></td>")
                elif day.coded:
                    output.append(
                        f"<td class='coded' style='background-color: green;'>{day.day}</td>"
                    )
                else:
                    output.append(f"<td>{day.day}</td>")
            output.append("</tr>")
        output.append("</table>")
        return "\n".join(output)


if __name__ == "__main__":
    coding_days = [1, 12, 30]
    cs = CodingStreak(2023, 9, coding_days)
    html = cs.create_streak_calendar_as_html()
    print(html)
