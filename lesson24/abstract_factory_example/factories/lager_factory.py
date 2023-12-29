from lesson24.abstract_factory_example.factories.factories import BeerFactory
from .sort_of_beer import  Ale, Lager


class LagerFactory(BeerFactory):
    _beer_type = 'lager'

    def __init__(self):
        self.name = 'Rogan'
        self._positions = ['lager', 'ale']


    @property
    def positions(self):
        return self._positions

    def brew_beer(self, name):
        if name == 'lager':
            return Lager()
        elif name == 'ale':
            return Ale()