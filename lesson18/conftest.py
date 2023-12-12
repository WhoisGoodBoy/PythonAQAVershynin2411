from selenium.webdriver import Chrome
import pytest
from lesson18.pages.dashboard_page import DashBoard
from lesson18.pages.category_page import Category



@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://nastolka.com.ua/uk')
    yield driver
    driver.quit()

@pytest.fixture
def dashboard(driver):
    yield DashBoard(driver)


@pytest.fixture
def category(driver):
    yield Category(driver)
