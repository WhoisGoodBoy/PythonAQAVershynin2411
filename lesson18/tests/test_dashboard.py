import time
from lesson18.core.CONSTANTS import list_of_logins, list_of_categories_names
import pytest
from selenium.webdriver.remote.webelement import WebElement
def test_check_choose_category_semejnye_igry(dashboard):
    family_category = dashboard.click_on_category()
    element:WebElement = family_category.wait_until_element_appears(family_category.locator_category_page_unique_element)
    header = family_category.wait_until_element_appears(family_category.locator_header)
    element_class = element.get_attribute('class')
    assert family_category.driver.current_url == 'https://nastolka.com.ua/uk/semejnye-igry'
    assert header.text == 'НАСТІЛЬНІ ІГРИ ДЛЯ ВСІЄЇ РОДИНИ'
    assert element.location['x'] == 490 and element.location['y'] == 415
    assert element_class == 'col catalog__content'


@pytest.mark.parametrize(
    'category_title', list_of_categories_names
)
def test_check_5_categories(dashboard, category_title):
    category = dashboard.click_on_category(category_title)
    assert category_title.lower() in category.driver.title

@pytest.mark.parametrize(
    'pair', [0]
)
def test_login(dashboard,pair):
    personal_cabinet = dashboard.bypass_login(pair)
    element = personal_cabinet.return_header()
    assert element.text == "ОСОБИСТИЙ КАБІНЕТ"


@pytest.mark.parametrize(
    'login,password', list_of_logins
)
def test_login2(dashboard,login, password):
    personal_cabinet = dashboard.bypass_login2(login, password)
    element = personal_cabinet.return_header()
    assert element.text == "ОСОБИСТИЙ КАБІНЕТ"
