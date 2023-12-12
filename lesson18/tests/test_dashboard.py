import time


def test_check_choose_category(dashboard):
    family_category = dashboard.click_on_family_category()

    time.sleep(5)