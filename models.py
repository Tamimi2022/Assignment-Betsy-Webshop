# Models go here
from peewee import *
import peewee

# A key part of the Betsy webshop is the database
# So we make a database = db
db = peewee.SqliteDatabase('besty_shop.db')


# A user has a name, address data, and billing information
# So we put on Class
class User(Model):
    username = CharField(unique=True, primary_key=True)
    password = CharField()
    address = CharField()
    country = CharField()
    city = TextField()
    postalcode = CharField()
    phone = IntegerField()
    billing = CharField()
    
    class Meta:
        database = db 
    
# The products must have a name, a description, a price per unit, and a quantity describing the amount in stock
class Product(Model):
    productname = CharField(null=False, primary_key=True)
    description = CharField()
    productprice = DecimalField(decimal_places=2, auto_round=True)
    quantity = IntegerField()
    
    class Meta:
        database = db
    
# The Tags
class Tag(Model):
    user = CharField(unique=True, null=False, primary_key=True) # TextField

    class Meta:
        database = db
# The Transactions model
# The transaction model must link a buyer with a purchased product and a quantity of purchased items
class Transaction(Model):
    id = BigAutoField(primary_key=True)
    buyer_id = ForeignKeyField(User, backref='get_user')
    seller_id = ForeignKeyField(User, backref='get_user')
    product_id = ForeignKeyField(Product, backref='get_product')
    quantity_items = IntegerField()
    totalprice = DecimalField(decimal_places=2, auto_round=True)
    
    class Meta:
        database = db
    
class ProductTag(Model):
    id = BigAutoField()
    product_id = ForeignKeyField(Product, backref='get_tags')
    tag_id = ForeignKeyField(Tag, backref='get_tags')
    
    class Meta:
        database = db
        
class UserProduct(Model):
    user = ForeignKeyField(User, backref='get_products')
    product = ForeignKeyField(Product, backref='get_products')
    
    class Meta:
        database = db