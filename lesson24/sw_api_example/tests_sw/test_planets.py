

def test_planet_1(planet_service):
    first_planet = planet_service.get_planet(1)
    planet_service.save_planet(1)
    assert first_planet.status_code == 200
    assert first_planet.json()['name'] == 'Tatooine'

def test_get_planets(planet_service):
    list_of_planets = planet_service.get_planets(2)
    assert list_of_planets.json()['next'] == 'https://swapi.dev/api/planets/?page=3'