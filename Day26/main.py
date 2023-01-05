weather_c = {
    "Monday": 12,
    "Tuesday": 14,
}

weather_f = {day:temp*1.8+32 for (day, temp) in weather_c.items()}
print(weather_f)