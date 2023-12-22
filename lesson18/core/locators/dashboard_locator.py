from lesson18.core.locators.base_locator import BaseLocator

class DashBoardLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.locator_catalogue = ('xpath','//div[@class="catalog-menu"]/a[text()="Каталог ігор"]')
        self.locator_login_email = ('xpath', '//input[@id="modal-enter-login"]')
        self.locator_login_password = ('xpath', '//input[@id="modal-enter-pass"]')
        self.locator_login_button = ('xpath', '//form[@id="login-form"]/div/button[@class="btn btn--full btn--primary"]')
        self.locator_login_succeful = ('xpath', '//div[@class="bottom d-flex"]/a[@href="profile"]')

    def return_parametrized_category_locator(self, category_title):
        self.locator_category = ('xpath', f'//div[@class="catalog-menu"]//li[@class="catalog-menu__item"]/a[@title="{category_title}"]')
        return self.locator_category
