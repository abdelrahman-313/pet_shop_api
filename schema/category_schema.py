from extension.extension import Extensions

ext = Extensions.getInstance()
ma = ext.get_ma()



class CategorySchema(ma.Schema):
    pet_categories = ma.List(ma.String)


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)