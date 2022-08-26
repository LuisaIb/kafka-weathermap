import json
from dataclasses import dataclass
from typing import Dict, Optional

import requests


@dataclass
class OpenWeatherMap:
    api_key: str
    base_url: str

    def __init__(self):
        self.api_key            = '8489db30088cf8d0026a5d5fd5a66b9f'
        self.base_url  = 'https://api.openweathermap.org/data/2.5'

    def build_url(self, city: json) -> str:
        static_params = 'units=metric&exclude=current,minutely,hourly,alerts&lang=de'
        url = f'{self.base_url}/forecast?lat={city["latitude"]}&lon={city["longitude"]}&appid={self.api_key}&{static_params}'
        return url

    def get_coordinates(self, city: str, country_code: str = None):
        if country_code is not None:
            city = f'{city},{country_code}'
        url = f'{self.base_url}/weather?q={city}&appid={self.api_key}'
        try:
            api_response = requests.get(url, verify=True, timeout=10)
            if api_response.ok:
                return json.loads(api_response.content)['coord']
        except Exception as e:
            print(f'    ! error while loading url {url}: {e}')
        return None

    def get_forecast(self, city: json) -> Optional[Dict]:
        url = self.build_url(city)
        try:
            api_response = requests.get(url, verify=True, timeout=10)
            if api_response.ok:
                return json.loads(api_response.content)
        except Exception as e:
            print(f'    ! error while loading url {url}: {e}')
        return None
