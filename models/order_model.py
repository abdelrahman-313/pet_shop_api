from extension.extension import Extensions


ext = Extensions.getInstance()
db = ext.get_db()

class Order(db.Model):
    __tablename__ = 'orders'
    # create pet id column
    id = db.Column(db.Integer, primary_key=True)
    # create pet name column
    order_name = db.Column(db.String(100), nullable=False)

    # f_pet_id = db.Column(db.Integer,db.ForeignKey('pets.pet_id'))

    pets = db.relationship('PetCategory', backref='pet')


# db.create_all()