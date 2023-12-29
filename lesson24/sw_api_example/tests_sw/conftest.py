
import pytest
from lesson24.sw_api_example.infrastructure.planets_service import PlanetService



@pytest.fixture()
def planet_service():
    return PlanetService()
