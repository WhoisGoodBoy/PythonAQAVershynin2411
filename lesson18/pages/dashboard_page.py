from lesson18.pages.base_page import BasePage
from lesson18.pages.category_page import Category
from lesson18.core.locators.dashboard_locator import DashBoardLocator
from lesson18.core.CONSTANTS import list_of_logins
import lesson18.pages.personal_cabinet_page
#try:
#    from lesson18.pages.personal_cabinet_page import PersonalCabinet
#except ImportError:
#    PersonalCabinet = None


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

    def open_login_form(self):
        self.click_on_element(self.locator.locator_login)

    def fill_email_field(self, email):
        self.send_text_to_element(self.locator.locator_login_email,email)

    def fill_password_field(self,password):
        self.send_text_to_element(self.locator.locator_login_password, password)

    def click_on_login_button(self):
        self.click_on_element(self.locator.locator_login_button)

    def bypass_login(self, pair=0):
        self.open_login_form()
        self.fill_email_field(list_of_logins[pair][0])
        self.fill_password_field(list_of_logins[pair][1])
        self.click_on_login_button()
        from lesson18.pages.personal_cabinet_page import PersonalCabinet
        return PersonalCabinet(self.driver)

    def bypass_login2(self, login,password):

        self.open_login_form()
        self.fill_email_field(login)
        self.fill_password_field(password)
        self.click_on_login_button()
        return lesson18.pages.personal_cabinet_page.PersonalCabinet(self.driver)

    def get_element_of_login_link(self):
        self.wait_until_element_appears(self.locator.locator_login_succeful)