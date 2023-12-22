from selenium.webdriver import Chrome
import pytest
from lesson18.pages.dashboard_page import DashBoard
from lesson18.pages.category_page import Category
from lesson18.pages.product_page import Product
import random

def get_random_value():
    return str(random.randint(100000,300000))


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def dashboard(driver):
    driver.get('https://nastolka.com.ua/uk')
    print(driver.get_cookie('_ga_6QK0BMVT8Q'))
    generated_cookie = get_random_value()
    driver.add_cookie({'name':'pespatron', 'value':f'__ua{generated_cookie}'})
    print(driver.get_cookie('pespatron'))
    driver.execute_script("window.localStorage['inlineSVGrev'] = 'White';")
    print(driver.execute_script("return window.localStorage['inlineSVGrev'];"))
    yield DashBoard(driver)


@pytest.fixture
def category(driver, category_link='uk/semejnye-igry'):
    driver.get(f'https://nastolka.com.ua/{category_link}')
    yield Category(driver)


@pytest.fixture
def product(driver):
    driver.get('https://nastolka.com.ua/uk/uzhas-arkhema-tretya-redakciya')
    yield Product(driver)
