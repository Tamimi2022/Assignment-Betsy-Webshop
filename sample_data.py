from models import *
from peewee import *


user_data = (
    (
        'ftamimi', 'Farid Attamimi', 'Centrum', 'Nederland', 'Amsterdam', '1011dd', '0123456789'
    )
)
for u in user_data:
    User.create(username=u[0], fullname=u[1], address=u[2], country=u[3], city=u[4], postalcode=u[5], billing=u[6])
    
product_data = (
    (
        'Rolex', 'Rolex Datejust 41', '98.99', '1'
    )
)
for p in product_data:
    Product.create(productname=p[0], description=p[1], productprice=p[2], quantity=p[3])
    
tag_data = (
    (
        'Rolex'
    )
)
for t in tag_data:
    Tag.create(name=t)
    
productTag_data = (
    (
        'Rolex', 'Rolex'
    )
)
for pt in productTag_data:
    ProductTag.create(product_id=pt[0], tag_owner=pt[1])
    
userProduct_data = (
    (
        'Farid Attamimi', 'Rolex'
    )
)
for up in userProduct_data:
    UserProduct.create(user=up[0], product=up[1])