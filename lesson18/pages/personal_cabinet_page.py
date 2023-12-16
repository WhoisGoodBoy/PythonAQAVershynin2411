import time

from lesson18.pages.base_page import BasePage
from lesson18.core.locators.personal_cabinet import PersonalCabinetLocator
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
        from lesson18.pages.dashboard_page import DashBoard
        self.click_on_element(self.locator.logo)
        self.driver.back()
        time.sleep(5)