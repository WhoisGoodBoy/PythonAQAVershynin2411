import pytest

from lesson25 import infrastructure as infra



@pytest.fixture
def single_object():
    yield infra.create_an_object()


@pytest.fixture
def single_obj_only_id(single_object):
    yield single_object.json()['id']