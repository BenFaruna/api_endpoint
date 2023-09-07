import os

import calendar
from datetime import datetime

import pytz

from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def api_route():
    query = request.args
    slack_name = query.get("slack_name")
    track = query.get("track")
    current_time = datetime.now(tz=pytz.utc)
    current_day = current_time.strftime("%Y-%m-%dT%H:%M:%SZ") #.isoformat(timespec="seconds")# + "Z"

    return jsonify({
        "slack_name": slack_name,
        "current_day": calendar.day_name[current_time.weekday()],
        "utc_time": current_day,
        "track": track,
        "github_file_url": os.getenv("github_file_url"),
        "github_file_repo": os.getenv("github_file_repo"), # environmental variable
        "status_code": 200
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=os.getenv("DEBUG"))
