class BaseLocator:
    def __init__(self):
        self.search = ('xpath', '//div[@class="bottom"]/form[@class="search js-search"]')
        self.locator_basket = ('xpath', '//div[@class="col header__forum"]/div[@class="bottom"]/div')
        self.locator_basket_proceed_to_basket = ('xpath', '//div[@class="tool js-dropdown isOpened"]/div[@class="header-basket tool__dropdown header_goods"]/a')
        self.locator_login = ('xpath', '//div[@class="bottom d-flex"]/a[text()="ВХІД"]')
        self.logo = ('xpath', '//a[@class="site-menu__logo"]')
        self.locator_hamburger_button = ('xpath', '//div[@class="col scroll-header__menu"]/button[@class="btn-reset menu-btn js-menu-toggle"]')
        self.locator_main_page_breadcrums = ('xpath', '//li[@class="breadcrumbs__item"]/a[text()="Головна"]')