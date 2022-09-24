__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

#from itertools import product

from site import main
from models import *
from decimal import Decimal
import peewee
from models import Model

    # Creating Table
db.connect()
db.create_tables([User, Product, Tag, Transaction, ProductTag, UserProduct])


def search(term):
    # Search for products based on a term
    query = Product.select().where(Product.productname.contains(term)) | (Product.description.contains(term))#.order_by(Product.productname).dicts()
    search_result = list(query.execute())
    if len(search_result) > 0:
        return search_result
    return []

def list_user_products(user_id):
    query = Product.select().join(UserProduct, on=(Product.productname == UserProduct.product)).join(
        User, on=(User.username == UserProduct.user)).where(User.username == user_id).dicts()
    search_result = list(query.execute())
    if len(search_result) > 0:
        return search_result
    return []

def list_products_per_tag(tag_id):
    query = Product.select().join(ProductTag, on=(Product.productname == ProductTag.product_id)).join(
        Tag, on=(Tag.user == ProductTag.tag_id)
    ).where(Tag.user == tag_id).dicts()
    search_result = list(query.execute())
    if len(search_result) > 0:
        return search_result
    return []

def add_product_to_catalog(user_id, product):
    
    Product.create(productname=product['productname'], description=product['description'], productprice=product['productprice'], quantity=product['quantity'])
    
    UserProduct.create(user=user_id, product=product['product']).save()
    return True

def update_stock(product_id, new_quantity):
    query = Product.update({Product.quantity: new_quantity}).where(Product.productname == product_id)
    search_result = query.execute()
    if search_result:
        return 'Success: 200'
    return 'Not Found'

def purchase_product(product_id, buyer_id, quantity):
    query_product = User.select(User.username).join(UserProduct, on=(User.username == UserProduct.user)).join(
        Product, on=(Product.productname == UserProduct.product)).where(
            Product.productname == product_id
        ).dicts()
    seller = list(query_product.execute())
    
    query_quantity = Product.select().where(Product.productname == product_id).dicts()
    product = list(query_quantity.execute())
    total = product[0]['productprice'] * quantity
    
    query_buyer = Transaction(buyer_id, seller_id=seller[0], product_id=product[0]['product_id'], quantity_items=quantity, totalprice=total)
    transaction = query_buyer.save()
    
    query_transaction = Transaction.select().where(Transaction.id == transaction)
    search_result = query_transaction.execute()
    if search_result:
        return True
    return False

def remove_product(product_id):
    query = UserProduct.delete().where(UserProduct.product == product_id)
    search_result = query.execute()
    if search_result:
        return True
    return False
print(update_stock('Keyboard', 999))

if __name__ == '__main__':
    main()