import requests
from datetime import datetime

APP_ID = "****"
API_KEY = "****"
APP_ENDPOINT = "****"
SHEET_ENDPOINT = "****"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
app_params = {
    "query": input("Which exercises you did?: "),
    "gender": "male",
    "weight_kg": "72.5",
    "height_cm": "170",
    "age": "28"
}

response = requests.post(url=APP_ENDPOINT, json=app_params, headers=headers)
response.raise_for_status()
data = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for i in data["exercises"]:
        sheet_inputs = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": i["name"].title(),
                "duration": i["duration_min"],
                "calories": i["nf_calories"]
            }
        }
        print(sheet_inputs)

        sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs)