from models import *
from peewee import *


def sample_data():
    attamimi = User.create(
        name='attamimi',
        address='centrum',
        billing='0123456789'
    )
    farid = User.create(
        name='farid',
        address='Utrecht',
        billing='9876543210'
    )
    
    rolex = Product.create(
        productname='rolex',
        description='Rolex Datejust 41',
        productprice=98.99,
        quantity=1,
        owner=attamimi
    )
    book = Product.create(
        productname='book',
        description='Novel book',
        productprice=40,
        quantity=4,
        owner=farid
    )
    
    watchmaking = Tag.create(name='watchmaking')
    
    ProductTag.create(product_id=rolex, tag_owner=watchmaking)

    publishing = Tag.create(name='publishing')

    ProductTag.create(product_id=book, tag_owner=publishing)

db.create_tables([User, Product, Tag, Transaction, ProductTag])
sample_data()