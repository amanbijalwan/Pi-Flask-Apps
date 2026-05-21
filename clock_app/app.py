from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

timezones = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Zurich": "Europe/Zurich",
    "Delhi": "Asia/Kolkata",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney"
}

@app.route("/", methods=["GET", "POST"])
def index():
    current_times = {}
    for city, tz in timezones.items():
        zone = pytz.timezone(tz)
        current_times[city] = datetime.now(zone).strftime("%Y-%m-%d %H:%M:%S")

    converted_time = None
    if request.method == "POST":
        from_city = request.form.get("from_city")
        to_city = request.form.get("to_city")
        input_time = request.form.get("input_time")

        if from_city and to_city and input_time:
            try:
                src_zone = pytz.timezone(timezones[from_city])
                dt = datetime.strptime(input_time, "%Y-%m-%d %H:%M:%S")
                src_dt = src_zone.localize(dt)

                target_zone = pytz.timezone(timezones[to_city])
                converted_time = src_dt.astimezone(target_zone).strftime("%Y-%m-%d %H:%M:%S")
            except Exception as e:
                converted_time = f"Error: {e}"

    return render_template("index.html", current_times=current_times,
                           timezones=list(timezones.keys()),
                           converted_time=converted_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
