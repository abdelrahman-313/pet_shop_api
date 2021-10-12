from models.pets_model import PetCategory
from models.order_model import Order
from extension.extension import Extensions
from flask_restful import abort
from sqlalchemy import and_

class DBManager:

    def __init__(self):
        ext = Extensions.getInstance()
        self.__db = ext.get_db()

    def insert_order(self, order_name, pets):
        new_order = Order(order_name=order_name, pets=pets)
        self.db_add_item(new_order)
        self.db_commit()
        return new_order

    def insert_pet(self, pet_name, pet_category, pet_price, pet_currency):
        new_pet = PetCategory(pet_name=pet_name, pet_category=pet_category,
                              pet_price=pet_price, pet_currency=pet_currency)
        self.db_add_item(new_pet)
        self.db_commit()
        return new_pet

    def get_pet(self, pet_id, filter_nulll=False):
        if filter_nulll:

            pets = PetCategory.query.get_or_404(pet_id,'this pet doesnot exist in shop')
            if pets.order_id:
                abort(404,description=f'requested pet with id ({pet_id}) is already sold out')

        else:
            pets = PetCategory.query.get_or_404(pet_id,'this pet doesnot exist in shop')

        return pets

    def get_pets(self):
        pets = PetCategory.query.all()
        return pets

    def get_pets_by_category(self, pet_category):
        pets = PetCategory.query.filter_by(pet_category=pet_category)
        return pets

    def delete_pet(self, pet_id):
        pet = PetCategory.query.get(pet_id)
        self.db_delete_item(pet)
        self.db_commit()
        return  pet

    def update_pet(self, pet_id, pet_name, pet_category, pet_price, pet_currency):
        pet = PetCategory.query.get(pet_id)
        pet.pet_name = pet_name
        pet.pet_category = pet_category
        pet.pet_price = pet_price
        pet.pet_currency = pet_currency
        self.__db.session.commit()
        return  pet

    def get_pet_categories(self):
        categories = PetCategory.query.with_entities(PetCategory.pet_category).distinct()
        categories_list = []
        for category in categories:
            categories_list.append(category.pet_category)
        return categories_list

    def db_commit(self):
        self.__db.session.commit()


    def db_add_item(self,added_item):
        self.__db.session.add(added_item)

    def db_delete_item(self,deleted_item):
        self.__db.session.delete(deleted_item)









db_manager = DBManager()