# import app from app.py
from extension.extension import Extensions
from schema.pets_schema import PetSchema
ext = Extensions.getInstance()
ma = ext.get_ma()

class OrderSchema(ma.Schema):

    class Meta:

        ordered = True
        fields = ("id","order_name","pets")

    pets = ma.Nested(PetSchema,many=True)


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)