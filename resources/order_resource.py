from flask_restful import  reqparse, Resource, Api
from dbManager.db_manager import db_manager
from schema.order_schema import order_schema,orders_schema
from schema.category_schema import category_schema, categories_schema




class Order(Resource):


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "order_name", type=str, required=True, help="order_name cannot be blank!"
        )
        parser.add_argument(
            "pet_ids", action='append' , required=True, help="pet_ids cannot be blank!"
        )

        args = parser.parse_args()
        pet_ids = args["pet_ids"]
        order_name = args['order_name']
        pets = []
        for pet_id in pet_ids:

            pet = db_manager.get_pet(pet_id,filter_nulll=True)
            pets.append(pet)

        new_order = db_manager.insert_order(order_name=order_name,pets=pets )
        return order_schema.jsonify(new_order)

