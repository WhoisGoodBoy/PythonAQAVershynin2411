from lesson24.abstract_factory_example.factories.stout_factory import StoutFactory
from lesson24.abstract_factory_example.factories.lager_factory import LagerFactory


class AbstractFactory:
    @staticmethod
    def get_factory(beer_type):
        if beer_type == 'lager':
            return LagerFactory()
        elif beer_type == 'stout':
            return StoutFactory()


stout_factory = AbstractFactory.get_factory('stout')
bottle_of_dry_stout = stout_factory.brew_beer('dry')
print(bottle_of_dry_stout)