
# import app from app.py
from extension.extension import Extensions

ext = Extensions.getInstance()
ma = ext.get_ma()

class PetSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("pet_id","pet_name","pet_category","pet_price","pet_currency")


pet_schema = PetSchema()
pets_schema = PetSchema(many=True)


# class PetFullSchema(ma.Schema):
#     class Meta:
#         ordered = True
#         fields = ("pet_id","pet_name","pet_category")
#
#
# pet_full_schema = PetFullSchema()
# pets_full_schema = PetFullSchema(many=True)