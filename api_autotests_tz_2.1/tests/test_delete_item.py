import pytest
from api import ItemAPI
from data.boundary_values import Boundary
from validators import ItemValidator
from data.item_factory import ItemFactory


def test_delete_item_positive():
    body = ItemFactory.valid_item()
    response = ItemAPI.create_item(body)
    ItemValidator.assert_status(response, [200])

    created_body = response.json()
    json = created_body["status"]

    item_id = json.split(" - ")[-1]

    get_resp = ItemAPI.get_item_by_id(item_id)
    ItemValidator.assert_status(get_resp, [200])

    delete = ItemAPI.delete_item_by_id(item_id)
    ItemValidator.assert_status(delete, [200])


@pytest.mark.parametrize("invald_id", Boundary.INVALID_IDS)
def test_delete_item_negative_invalid_id(invalid_id):
    response = ItemAPI.delete_item_by_id(invalid_id)
    ItemValidator.assert_status(response, [400])


def test_delete_item_negative_not_found():

    non_existing_id = ItemFactory.non_existing_id()

    response = ItemAPI.delete_item_by_id(non_existing_id)
    ItemValidator.assert_status(response, [404])
