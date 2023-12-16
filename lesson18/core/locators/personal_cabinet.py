from .base_locator import BaseLocator


class PersonalCabinetLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.header = ('xpath', '//div[@class="title title--lg page__title"]')