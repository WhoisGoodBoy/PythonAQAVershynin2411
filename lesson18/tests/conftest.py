from selenium.webdriver import Chrome
import pytest
from lesson18.pages.dashboard_page import DashBoard
from lesson18.pages.category_page import Category
from lesson18.pages.product_page import Product



@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def dashboard(driver):
    driver.get('https://nastolka.com.ua/uk')
    yield DashBoard(driver)


@pytest.fixture
def category(driver):
    driver.get('https://nastolka.com.ua/uk/semejnye-igry')
    yield Category(driver)


@pytest.fixture
def product(driver):
    driver.get('https://nastolka.com.ua/uk/uzhas-arkhema-tretya-redakciya')
    yield Product(driver)
