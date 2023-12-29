from selenium.webdriver import Firefox
from lesson24.factory_example.drivers.base_browser import Browser


class FirefoxBrowser(Browser):
    _name = 'firefox'


    def __init__(self):
        super().__init__()
        self.driver = Firefox()