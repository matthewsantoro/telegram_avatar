from time import sleep

import requests
from config import weather_api, CITY_ID
from utils import *


def get_current_weather():
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'id': CITY_ID, 'units': 'metric', 'lang': 'ru', 'APPID': weather_api})
    data = res.json()
    return {'temp': data['main']['temp'],
            'icon': data['weather'][0]['icon']}


print(get_current_weather())
print(get_current_weather())