import pytest
from extension.extension import Extensions


@pytest.fixture(scope='session')
def test_app():
    ext = Extensions.getInstance('test')
    app = ext.get_app()
    ext.add_end_points()
    with app.test_client() as testing_client:
        yield testing_client


@pytest.fixture(scope='session')
def get_last_pet_id():
    from models.pets_model  import PetCategory
    last_item_id = 0

    descending = PetCategory.query.order_by(PetCategory.pet_id.desc())
    last_item = descending.first()
    last_item_id = last_item.pet_id


    return last_item_id