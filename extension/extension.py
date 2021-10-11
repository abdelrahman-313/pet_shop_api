from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
import os
# from resources.pet_resource import Pet, PetCategoryList, PetList


class Extensions:
    __instance = None

    @staticmethod
    def getInstance(mode='dev'):
        """ Static access method. """
        if Extensions.__instance == None:
            Extensions(mode)
        return Extensions.__instance

    def __init__(self,mode):
        """ Virtually private constructor. """
        if Extensions.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.__app = Flask(__name__,instance_relative_config=True)
            base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            parent_folder_path = os.path.join(base_path,'config')
            if mode == 'test':
                config_file = os.path.join(parent_folder_path,'flask_test.py')
            else:
                config_file = os.path.join(parent_folder_path, 'flask.py')

            self.__app.config.from_pyfile(config_file)

            self.__db = SQLAlchemy(self.__app)

            self.__ma = Marshmallow(self.__app)

            self.__api = Api(self.__app)
            Extensions.__instance = self
            from models import pets_model
            self.__db.create_all()

    def get_app(self):
        return self.__app


    def get_db(self):

        return self.__db

    def get_ma(self):
        return self.__ma

    def get_api(self):
        return self.__api

    def add_end_points(self):
        from resources.pet_resource import Pet, PetCategoryList, PetList, PetsPerCategory
        from resources.order_resource import Order
        api = self.get_api()
        self.__app.config['JSON_SORT_KEYS'] = False

        api.add_resource(Pet, '/v1/pet/', '/v1/pet/<int:pet_id>')
        api.add_resource(PetsPerCategory, '/v1/pets/<string:pet_category>')
        api.add_resource(PetList, '/v1/pets/')
        api.add_resource(PetCategoryList, '/v1/pet_categories')
        api.add_resource(Order, '/v1/order/')








