from lesson18.pages.base_page import BasePage
from lesson18.pages.basket_page import BasketPage


class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_header = ('xpath', '//h1')
        self.locator_buy = ('xpath', '//div[@class="game__buy"]/a[1]')
        self.locator_popup_buy_close = ('xpath', '//button[@title="Close (Esc)"]')

    def buy_product(self):
        self.click_on_element(self.locator_buy)

    def close_popup(self):
        self.click_on_element(self.locator_popup_buy_close)

    def open_basket(self):
        self.click_on_element(self.locator_basket)

    def click_on_proceed_to_basket(self):
        self.click_on_element(self.locator_basket_proceed_to_basket)

    def proceed_to_basket(self):
        self.open_basket()
        self.click_on_proceed_to_basket()
        return BasketPage(self.driver)


