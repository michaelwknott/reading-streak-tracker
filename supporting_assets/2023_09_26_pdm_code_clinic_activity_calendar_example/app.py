# app.py
from datetime import datetime

from db import CodingDay, db
from flask import Flask, redirect, render_template_string, request, url_for
from script import CodingStreak

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/<int:year>/<int:month>")
def show_calendar(year, month):
    coding_days = CodingDay.get_coding_days(year, month)
    cs = CodingStreak(year, month, coding_days)
    html_calendar = cs.create_streak_calendar_as_html()
    return render_template_string(
        """<html>
    <head>
        <title>Coding Streak Calendar</title>
        <style>
            table {
                width: 50%;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 18px;
                text-align: left;
            }
            th, td {
                padding: 10px;
                border-bottom: 1px solid #ddd;
            }
            th {
                background-color: #f2f2f2;
            }
            .coded {
                background-color: green;
                color: white;
            }
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <form method="POST" action="{{ url_for('add_coding_day') }}">
            <label for="date">Add Coding Day:</label>
            <input type="date" id="date" name="date">
            <input type="submit" value="Add">
        </form>
        {{ html_calendar|safe }}
    </body>
</html>""",
        html_calendar=html_calendar,
    )


@app.route("/add_coding_day", methods=["POST"])
def add_coding_day():
    date_str = request.form.get("date")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_coding_day = CodingDay(date=date_obj)
    db.session.add(new_coding_day)
    db.session.commit()
    return redirect(url_for("show_calendar", year=date_obj.year, month=date_obj.month))


@app.route("/delete_coding_day/<int:id>")
def delete_coding_day(id):
    coding_day = CodingDay.query.get(id)
    if coding_day:
        db.session.delete(coding_day)
        db.session.commit()
    return redirect(request.referrer)


if __name__ == "__main__":
    # Create tables on startup
    with app.app_context():
        db.create_all()
    app.run(debug=True)
