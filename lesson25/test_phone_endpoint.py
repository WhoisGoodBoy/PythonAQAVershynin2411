import requests

from lesson25 import infrastructure as infra


def test_single_object_good_response():
    received_object = infra.get_single_object(1)
    assert received_object.status_code == 200

def test_create_single_object():
    new_object = infra.create_an_object()
    assert new_object.status_code == 200
    checked_object = infra.get_single_object(new_object.json()['id'])
    assert checked_object.status_code == 200
    assert new_object.json()['id'] == checked_object.json()['id']


def test_update_one_object():
    new_object = infra.create_an_object()
    updated_object = infra.update_the_object(new_object.json()['id'])
    assert updated_object.status_code == 200
    print(updated_object.json())

def test_patch_one_object(single_obj_only_id):
    patched_object = infra.patch_object(single_obj_only_id)
    assert patched_object.json()['data']['year'] == 208


def test_delete_single_object():
    new_object = infra.create_an_object()
    deleted_object = infra.delete_object(new_object.json()['id'])
    assert 'has been deleted' in deleted_object.json()['message']