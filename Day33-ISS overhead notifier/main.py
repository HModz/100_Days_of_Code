import requests
from datetime import datetime

MY_LAT = 0
MY_LONG = 0


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if iss_overhead() and is_night():
    print("Look up!")
