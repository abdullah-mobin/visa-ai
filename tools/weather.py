import requests

# Dhaka default (adjust as needed)
LAT = 23.81
LON = 90.41

def get_current_weather(lat=LAT, lon=LON):
    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true"
        )
        response = requests.get(url)
        data = response.json()

        if "current_weather" in data:
            weather = data["current_weather"]
            temp = weather["temperature"]
            wind = weather["windspeed"]
            condition = f"Temperature: {temp}°C, Wind Speed: {wind} km/h"
            return condition
        else:
            return "⚠️ Couldn't fetch weather info."
    except Exception as e:
        return f"❌ Weather error: {e}"
