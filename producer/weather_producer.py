import requests
import json
import time
from datetime import datetime

# Cairo coordinates (you can change)
LAT = 30.0444
LON = 31.2357

URL = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={LAT}&longitude={LON}"
    f"&current_weather=true"
)

OUTPUT_FILE = "/home/bigdata/usecase/weather.json"

while True:
    try:
        response = requests.get(URL)
        data = response.json()

        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "location": "Cairo",
            "source": "open-meteo",
            "weather": data.get("current_weather", {})
        }

        with open(OUTPUT_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")

        print("Written:", event)

    except Exception as e:
        print("Error:", e)

    time.sleep(10)