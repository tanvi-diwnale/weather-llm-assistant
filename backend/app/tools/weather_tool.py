import requests
from app.config import OPENWEATHER_API_KEY

def get_weather(city: str) -> str:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        return f"Unable to fetch weather for {city}"

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"It’s {temp}°C in {city} with {description}."
