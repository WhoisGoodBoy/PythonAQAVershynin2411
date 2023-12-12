from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_with_wait(driver, locator, seconds_to_wait):
    web_driver_wait = WebDriverWait(driver, seconds_to_wait)
    element = web_driver_wait.until(EC.presence_of_element_located(('xpath', locator)))
    return element



def test_01():
    driver = Chrome()
    driver.get('https://www.google.com/')
    driver.implicitly_wait(5)
    locator_input = '//textarea[@title="Пошук"]'
    element_input = driver.find_element(by='xpath', value=locator_input)
    element_input.send_keys('повернись живим')
    locator_first_element = '//div[@role="option"][@aria-label="повернись живим"]'
    element_first_element = driver.find_element('xpath', locator_first_element)
    element_first_element.click()



def test_02():
    driver = Chrome()
    driver.get('https://www.google.com/')
    web_driver_wait = WebDriverWait(driver, 10)
    locator_input = '//textarea[@title="Пошук"]'
    element_input = click_with_wait(driver,locator_input,10)
    element_input.send_keys('повернись живим')
    locator_first_element = '//div[@role="option"][@aria-label="повернись живим"]'
    element_first_element = click_with_wait(driver,locator_first_element,10)
    element_first_element.click()