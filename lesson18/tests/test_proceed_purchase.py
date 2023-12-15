


def test_proceed_purchase(dashboard):
    category = dashboard.click_on_family_category()
    product = category.click_on_first_element()
    product.buy_product()
    product.close_popup()
    basket = product.proceed_to_basket()
    