import pytest
from lesson15.len_example import Building, Company

@pytest.fixture
def building():
    print('setup for test')
    yield Building('a','b')


@pytest.fixture
def first_company():
    print('we`re creating first company')
    yield Company('first','building')

@pytest.fixture
def second_company():
    print('we`re creating second company')
    yield Company('second','building')

@pytest.fixture
def building_with_two_companies_inside(building,first_company,second_company):
    building_with_two_companies = building
    building_with_two_companies[1] = first_company
    building_with_two_companies[2] = second_company
    yield building_with_two_companies
