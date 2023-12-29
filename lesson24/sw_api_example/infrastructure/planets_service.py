from requests import get
import json
from lesson24.sw_api_example.conf import config


class PlanetService:
    def __init__(self):
        self.__planet_url = f'{config["host1"]}planets'

    def get_planet(self, planet_id):
        return get(f'{self.__planet_url}/{planet_id}')


    def get_planets(self, pagination_page=1):
        return get(f'{self.__planet_url}/?page={pagination_page}')

    def save_planet(self, planet_id):
        response = self.get_planet(planet_id)
        with open(f"{response.json()['name']}.json", 'w') as planet_data:
            json.dump(response.json(),planet_data,  indent=4)

