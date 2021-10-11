from flask_restful import abort, marshal_with, reqparse, Resource, Api
from dbManager.db_manager import db_manager
from schema.pets_schema import pets_schema,pet_schema
from schema.category_schema import category_schema, categories_schema




class Pet(Resource):

    def get(self, pet_id):
        pet = db_manager.get_pet(pet_id=pet_id)
        return pet_schema.jsonify(pet)



    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "pet_name", type=str, required=True, help="pet_name cannot be blank!"
        )
        parser.add_argument(
            "pet_category", type=str, required=True, help="pet_category cannot be blank!"
        )
        parser.add_argument(
            "pet_price", type=float, required=True, help="pet_price cannot be blank!"
        )

        parser.add_argument(
            "pet_currency", type=str, required=True, help="pet_currency cannot be blank!"
        )
        args = parser.parse_args()
        pet_name = args["pet_name"]
        pet_category = args["pet_category"]
        pet_price = args["pet_price"]
        pet_currency = args["pet_currency"]

        new_pet = db_manager.insert_pet(pet_name=pet_name,
                                        pet_category= pet_category,
                                        pet_price= pet_price,
                                        pet_currency= pet_currency )
        return pet_schema.jsonify(new_pet)

    def delete(self, pet_id):
        pet = db_manager.delete_pet(pet_id=pet_id)
        return pet_schema.jsonify(pet)

    def put(self,pet_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "pet_name", type=str, required=True, help="pet_name cannot be blank!"
        )
        parser.add_argument(
            "pet_category", type=str, required=True, help="pet_category cannot be blank!"
        )
        parser.add_argument(
            "pet_price", type=float, required=True, help="pet_price cannot be blank!"
        )

        parser.add_argument(
            "pet_currency", type=str, required=True, help="pet_currency cannot be blank!"
        )
        args = parser.parse_args()
        pet_name = args["pet_name"]
        pet_category = args["pet_category"]
        pet_price = args["pet_price"]
        pet_currency = args["pet_currency"]

        update_pet = db_manager.update_pet(pet_id=pet_id,
                                            pet_name=pet_name,
                                            pet_category=pet_category,
                                            pet_price=pet_price,
                                            pet_currency=pet_currency)
        return pet_schema.jsonify(update_pet)


class PetList(Resource):
    def get(self):
        pet = db_manager.get_pets()
        return pets_schema.jsonify(pet)


class PetCategoryList(Resource):

    def get(self):
        categories = db_manager.get_pet_categories()
        print(categories)
        resource_output = {'pet_categories':categories}
        return category_schema.dump(resource_output)

class PetsPerCategory(Resource):

    def get(self, pet_category):
        pets = db_manager.get_pets_by_category(pet_category=pet_category)
        return pets_schema.jsonify(pets)
