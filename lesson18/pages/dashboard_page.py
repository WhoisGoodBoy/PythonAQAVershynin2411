from lesson18.pages.base_page import BasePage
from lesson18.pages.category_page import Category


class DashBoard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_catalogue = ('xpath','//div[@class="catalog-menu"]/a[text()="Каталог ігор"]')
        self.locator_for_family = ('xpath','//div[@class="catalog-menu"]//li[@class="catalog-menu__item"]/a[@title="Для всієї родини"]')

    def click_on_catalogue(self):
        self.click_on_element(self.locator_catalogue)

    def click_on_family_category(self):
        self.click_on_catalogue()
        self.click_on_element(self.locator_for_family)
        return Category(self.driver)

