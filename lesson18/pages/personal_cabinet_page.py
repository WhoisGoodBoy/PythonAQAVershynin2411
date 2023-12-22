import time

from lesson18.pages.base_page import BasePage
from lesson18.core.locators.personal_cabinet import PersonalCabinetLocator
import lesson18.pages.dashboard_page as dashboard_page
'''
try:
    from lesson18.pages.dashboard_page import DashBoard
except ImportError:
    DashBoard = None
'''
# Rest of the code


class PersonalCabinet(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = PersonalCabinetLocator()

    def return_header(self):
        return self.wait_until_element_appears(self.locator.header)

    def got_to_main_page(self):
        time.sleep(3)
        self.click_on_element(self.locator.locator_hamburger_button)
        time.sleep(3)
        self.click_on_element(self.locator.logo)
        #self.driver.back()
        return dashboard_page.DashBoard(self.driver)

    def got_to_main_page2(self):
        self.click_on_element(self.locator.locator_main_page_breadcrums)
        #self.driver.back()
        return dashboard_page.DashBoard(self.driver)