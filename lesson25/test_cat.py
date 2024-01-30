import pytest
from lesson25 import infrastructure as infra


@pytest.mark.regression
def test_cat_creation():
    list_of_cats_actual,  list_of_cats_expected = infra.filter_cats_and_only_cats()
    for cat in list_of_cats_expected:
        cat_dict= {'id':cat._id, 'name':cat.data['name'], 'data':cat.data['data']}
        assert cat_dict in list_of_cats_actual
        print(cat_dict)
