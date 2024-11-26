import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from tests.test_data import payloads


@pytest.mark.parametrize('payload', payloads.create_payloads)
def test_create_object(all_tests, payload):
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_name(name=payload['name'])
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_data(data=payload['data'])


def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object(obj_id)
    get_object_endpoint.check_id(obj_id)
    get_object_endpoint.check_response_is_200()


@pytest.mark.parametrize('payload', payloads.upload_payloads)
def test_put_object(obj_id, payload):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_object(payload=payload, obj_id=obj_id)
    update_object_endpoint.check_name_update(name=payload['name'])
    update_object_endpoint.check_response_is_200()


def test_delete_object(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_by_id(obj_id)
    delete_object_endpoint.check_response_is_200()
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_404()