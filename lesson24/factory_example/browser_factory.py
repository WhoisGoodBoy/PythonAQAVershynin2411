from lesson24.factory_example.drivers import ChromeBrowser, FirefoxBrowser


class BrowserFactory:
    def __init__(self):
        self.last_browser = None


    def get_browser(self, name):
        self.last_browser = name
        if name == 'chrome':
            return ChromeBrowser()
        elif name == 'firefox':
            return FirefoxBrowser()
        else:
            raise Exception('wrong type')


browser_factory = BrowserFactory()
chrome1 = browser_factory.get_browser('chrome')
chrome2 = browser_factory.get_browser('chrome')
firefox = browser_factory.get_browser('firefox')
print()