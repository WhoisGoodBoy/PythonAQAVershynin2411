



def test_go_to_first_element(dashboard):
    category = dashboard.click_on_family_category()
    first_product_in_the_list = category.click_on_first_element()
    header = first_product_in_the_list.wait_until_element_appears(first_product_in_the_list.locator_header)
    assert header.text == 'ЖАХ АРКХЕМУ. ТРЕТЯ РЕДАКЦІЯ (УКР.)'
    assert first_product_in_the_list.driver.current_url == 'https://nastolka.com.ua/uk/uzhas-arkhema-tretya-redakciya'

