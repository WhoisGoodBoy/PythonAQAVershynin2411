from selenium.webdriver import Chrome
from lesson24.factory_example.drivers.base_browser import Browser



class ChromeBrowser(Browser):
    _name = 'chrome'

    def __init__(self):
        super().__init__()
        self.driver = Chrome()