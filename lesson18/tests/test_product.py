import pytest



def test_check_header(product):
    header = product.wait_until_element_appears(product.locator_header)
    assert header.text == 'ЖАХ АРКХЕМУ. ТРЕТЯ РЕДАКЦІЯ (УКР.)'
    assert product.driver.current_url == 'https://nastolka.com.ua/uk/uzhas-arkhema-tretya-redakciya'


def test_check_header_with_diff_driver(product2):
    header = product2.wait_until_element_appears(product2.locator_header)
    assert header.text == 'ЖАХ АРКХЕМУ. ТРЕТЯ РЕДАКЦІЯ (УКР.)'
    assert product2.driver.current_url == 'https://nastolka.com.ua/uk/uzhas-arkhema-tretya-redakciya'
