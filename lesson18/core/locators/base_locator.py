class BaseLocator:
    def __init__(self):
        self.search = ('xpath', '//div[@class="bottom"]/form[@class="search js-search"]')
        self.locator_basket = ('xpath', '//div[@class="col header__forum"]/div[@class="bottom"]/div')
        self.locator_basket_proceed_to_basket = ('xpath', '//div[@class="tool js-dropdown isOpened"]/div[@class="header-basket tool__dropdown header_goods"]/a')
