from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def test_01():
    driver = Chrome()
    driver.get('https://www.google.com/')
    locator_input = '//textarea[@title="Пошук"]'
    element_input = driver.find_element(by='xpath', value=locator_input)
    element_input.send_keys('повернись живим')
    locator_first_element = '//div[@role="option"][@aria-label="повернись живим"]'
    element_first_element = driver.find_element('xpath', locator_first_element)
    element_first_element.click()
    time.sleep(7)
    locator_first_search_result = '//a[@href="https://savelife.in.ua/"]'
    element_first_search_result = driver.find_element('xpath', locator_first_search_result)
    element_first_search_result.click()
    time.sleep(7)
    driver.quit()


def test_02():
    driver = Chrome()
    driver.get('https://duckduckgo.com/')
    locator_input = '//input[@id="searchbox_input"]'
    element_input = driver.find_element('xpath', locator_input)
    element_input.send_keys('atlantida')
    element_input.send_keys(Keys.ENTER)
    time.sleep(5)

def test_03():
    driver = Chrome()
    driver.get('https://duckduckgo.com/')
    locator_input = '//input[@id="searchbox_input"]'
    element_input = driver.find_element('xpath', locator_input)
    element_input.send_keys('atlantida')
    actions = ActionChains(driver)
    time.sleep(2)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    actions.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()
    time.sleep(5)


class ByTheWay:
    amount = 1