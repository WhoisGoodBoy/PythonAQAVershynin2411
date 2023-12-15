import time
from selenium.webdriver.remote.webelement import WebElement
def test_check_choose_category_semejnye_igry(dashboard):
    family_category = dashboard.click_on_family_category()
    element:WebElement = family_category.wait_until_element_appears(family_category.locator_category_page_unique_element)
    header = family_category.wait_until_element_appears(family_category.locator_header)
    element_class = element.get_attribute('class')
    assert family_category.driver.current_url == 'https://nastolka.com.ua/uk/semejnye-igry'
    assert header.text == 'НАСТІЛЬНІ ІГРИ ДЛЯ ВСІЄЇ РОДИНИ'
    assert element.location['x'] == 490 and element.location['y'] == 415
    assert element_class == 'col catalog__content'

