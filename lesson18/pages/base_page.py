from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson18.core.locators.base_locator import BaseLocator


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(self.driver, 10)
        self.locator = BaseLocator()


    def wait_until_element_appears(self, locator:tuple):
        element = self.web_driver_wait.until(EC.presence_of_element_located(locator))
        return element

    def click_on_element(self, locator):
        element = self.wait_until_element_appears(locator)
        element.click()

    def send_text_to_element(self, locator, text):
        element = self.wait_until_element_appears(locator)
        element.send_keys(text)
        