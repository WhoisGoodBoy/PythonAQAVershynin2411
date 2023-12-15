from lesson18.pages.base_page import BasePage
from lesson18.pages.product_page import Product


class Category(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_header = ('xpath', '//h1')
        self.locator_category_page_unique_element = ('xpath', '//div[@id="goods_catalog"]')
        self.locator_first_element = ('xpath', '//div[@class="product-list viewTilesSm"]/div[1]/a[1]')

    def click_on_first_element(self):
        self.click_on_element(self.locator_first_element)
        return Product(self.driver)

