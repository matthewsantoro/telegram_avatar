import requests
from config import WEATHER_API, CITY_ID


def get_current_weather():
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'id': CITY_ID, 'units': 'metric', 'lang': 'ru', 'APPID': WEATHER_API})
    data = res.json()
    return {'temp': data['main']['temp'],
            'icon': data['weather'][0]['icon']}


