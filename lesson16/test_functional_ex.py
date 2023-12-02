from lesson15.len_example import Building,Company
import pytest


@pytest.mark.smoke
@pytest.mark.xfail(reason='fail due to existing bug', condition=True)
def test_len(building):
    assert len(building) == 1


@pytest.mark.skip('this part is on the maintenance')
def test_len_one_company_added(building):
    building[1] = Company('c','d')
    assert len(building) == 1


@pytest.mark.regression
def test_len_two_companies(building, first_company, second_company):
    building[1] = first_company
    building[2] = second_company
    assert len(building) == 2


@pytest.mark.smoke
@pytest.mark.regression
def test_two_companies_building_with_fixture(building_with_two_companies_inside):
    assert len(building_with_two_companies_inside) == 2


@pytest.mark.parametrize(
    'company_name,expected_name,address,expected_address',[('first_name','first_name', 'first_address', 'first_address'), ('second_name', 'second_name', 'second_address', 'second_address')],ids=['testing_first_name', 'testing_second_name']
)
def test_parametrised_companies(building, company_name, expected_name, address, expected_address):
    building[1] = Company(company_name, address)
    assert building[1].name == expected_name
    assert building[1].industry == expected_address


@pytest.mark.parametrize(
    'company,expected_name,expected_address',[(Company('first_name', 'first_address'),'first_name', 'first_address'), (Company('second_name', 'second_address'),'second_name', 'second_address')],ids=['testing_first_name', 'testing_second_name']
)
def test_parametrised_companies_added(building, company, expected_name, expected_address):
    building[1] = company
    assert building[1].name == expected_name
    assert building[1].industry == expected_address

