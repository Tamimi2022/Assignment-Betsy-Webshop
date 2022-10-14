__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

#from itertools import product
from models import *
from decimal import Decimal
import peewee
from models import Model

    # Creating Table
db.close()
db.connect()
db.create_tables([User, Product, Tag, Transaction, ProductTag])


def search(term):
    # Search for products based on a term
    query = Product.select().where(Product.productname.contains(term) | (Product.description.contains(term)))
    search_result = list(query.execute())
    if len(search_result) > 0:
        return search_result
    return 'search'


def list_user_products(user_id):
    try:
        user = User.get_by_id(user_id)
        products = Product.select().where(Product.owner == user).join(User)
        
        if len(products) > 0:
            print(f'{user.name}')
            for p in products:
                return(
                    f'Product: {p.productname}, price per unit: {p.productprice}, availabilty: {p.quantity}'
                )
        else:
            print(
                f'{user.name} has no products available '
            )
    except Exception:
        print('Not found')
        

def list_products_per_tag(tag_id):
    query = Product.select().join(ProductTag).where(ProductTag.tag_owner == tag_id)
    
    if len(query) > 0:
        print(f'Available products:')
        for q in query:
            print(
                f'Product: {q.productname}, price per unit: {q.productprice}, availabilty: {q.quantity}'
            )
    else:
        print('no products found')
        

def add_product_to_catalog(user_id, product):
    
    Product.create(productname=product['productname'], description=product['description'], productprice=product['productprice'], quantity=product['quantity'], owner=user_id)
    print(f'We have now {product["quantity"]} items {product["productname"]} added to your products')


def update_stock(product_id, new_quantity):
    try:
        query = Product.update({Product.quantity: new_quantity}).where(Product.productname == product_id)
        query.execute()
        print(f'Product stock {Product.get_by_id(product_id).productname} has been modified to {new_quantity}')
    except Exception:
        print('This product is not available, So enter as new product')


def purchase_product(product_id, buyer_id, quantity):
    try:
        product = Product.get_by_id(product_id)
        
        if product.quantity >= quantity:
            product.quantity = product.quantity - quantity
            Transaction.create(
                buyer=buyer_id,
                product_id=product_id,
                quantity=quantity
            )
            new_quantity = (product.quantity - quantity)
            print(f'well, you buy {quantity} x {product.productname} front of {product.productprice} per item')
            update_stock(product_id, new_quantity)
        else:
            print(f'There are {product.quantity} items {product.productname} available, now adjust the quantity')
    except Exception:
        print('This product is not available')
        
        
def remove_product(product_id):
    try:
        product = Product.delete_by_id(product_id)
        print(f'{product.productname} is removed')
    except Exception:
        print(f'No product available with id {product_id}')
        
