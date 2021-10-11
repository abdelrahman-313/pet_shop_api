# import app, db from app.py
from extension.extension import Extensions

from models.order_model import Order


ext = Extensions.getInstance()
db = ext.get_db()

# pet category class 
class PetCategory(db.Model):
   __tablename__ = 'pets'
   # create pet id column
   pet_id = db.Column(db.Integer, primary_key = True)
  
   # create pet name column
   pet_name = db.Column(db.String(100), nullable = False)
  
   # create pet category column
   pet_category = db.Column(db.String(100), nullable = False )

   # create pet price column
   pet_price = db.Column(db.Float(), nullable = False)

   #create pet currency column
   pet_currency = db.Column(db.String(50), nullable = False)

   order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))


