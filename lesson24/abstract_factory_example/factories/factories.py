from abc import ABC, abstractmethod


class BeerFactory(ABC):
    _beer_type = ''


    @abstractmethod
    def brew_beer(self, name):
        pass