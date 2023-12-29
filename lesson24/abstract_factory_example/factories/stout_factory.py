from lesson24.abstract_factory_example.factories.factories import BeerFactory
from .sort_of_beer import Dry, Milk


class StoutFactory(BeerFactory):
    _beer_type = 'stout'

    def __init__(self):
        self.name = 'Dykansky Vechory'
        self._positions = ['milk', 'dry']

    @property
    def positions(self):
        return self._positions

    def brew_beer(self, name):
        if name == 'dry':
            return Dry()
        elif name == 'milk':
            return Milk()