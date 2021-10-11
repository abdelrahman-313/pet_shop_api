import pytest
from tests.configtest import test_app, get_last_pet_id
from extension.extension import Extensions
import json


insert_values = [{'pet_name':'popi','pet_category':'german','pet_price':120,'pet_currency':'$'}]

update_values = [{'pet_name':'popi_2','pet_category':'german_2','pet_price':320,'pet_currency':'$'}]

@pytest.mark.parametrize('case',insert_values)
def test_add_pet(test_app,case):

    response = test_app.post('/v1/pet/',data=case)
    assert response.status_code == 200


def test_order_creation(test_app,get_last_pet_id):
    orders = {
        "order_name": "selling_order",
        "pet_ids": [get_last_pet_id]
    }
    orders_2 = {
        "order_name": "selling_order",
        "pet_ids": [get_last_pet_id]
    }
    response = test_app.post('/v1/order/',data=orders)
    response_2 = test_app.post('/v1/order/',data=orders_2)
    assert response.status_code == 200
    assert response_2.status_code == 404



def test_get_pet_by_id(test_app,get_last_pet_id):

    response = test_app.get(f'/v1/pet/{get_last_pet_id}')
    assert response.status_code == 200


@pytest.mark.parametrize('case', update_values)
def test_update_pet(test_app, get_last_pet_id, case):
    response = test_app.put(f'/v1/pet/{get_last_pet_id}',data=case)
    assert response.status_code == 200



def test_get_pets(test_app):
    response = test_app.get('/v1/pets/')
    assert response.status_code == 200

def test_get_pet_categories(test_app):
    response = test_app.get('/v1/pet_categories')
    assert response.status_code == 200

def test_get_pets_per_category(test_app):
    category = update_values[0]['pet_category']
    response = test_app.get(f'/v1/pets/{category}')
    assert response.status_code == 200

def test_delete_pet(test_app,get_last_pet_id):
    response = test_app.delete(f'/v1/pet/{get_last_pet_id}')
    assert response.status_code == 200
