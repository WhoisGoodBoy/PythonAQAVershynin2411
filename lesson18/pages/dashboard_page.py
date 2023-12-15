from lesson18.pages.base_page import BasePage
from lesson18.pages.category_page import Category
from lesson18.core.locators.dashboard_locator import DashBoardLocator


class DashBoard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = DashBoardLocator()

    def click_on_catalogue(self):
        self.click_on_element(self.locator.locator_catalogue)

    def click_on_family_category(self):
        self.click_on_catalogue()
        self.click_on_element(self.locator.locator_for_family)
        return Category(self.driver)

