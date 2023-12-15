from lesson18.core.locators.base_locator import BaseLocator

class DashBoardLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.locator_catalogue = ('xpath','//div[@class="catalog-menu"]/a[text()="Каталог ігор"]')
        self.locator_for_family = ('xpath','//div[@class="catalog-menu"]//li[@class="catalog-menu__item"]/a[@title="Для всієї родини"]')

