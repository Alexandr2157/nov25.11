import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "test_data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(create_object.response_json['id'])


@pytest.fixture(scope='session')
def all_tests():
    print('Start tests all')
    yield
    print(' Finish tests all')