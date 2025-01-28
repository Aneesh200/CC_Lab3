import json
from typing import List
import products
from cart import dao
from products import Product

class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> 'Cart':
        return Cart(data['id'], data['username'], data['contents'], data['cost'])

def get_cart(username: str) -> List[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []
    
    items = []
    for cart_detail in cart_details:
        try:
            # Use json.loads instead of eval for safety
            contents = json.loads(cart_detail['contents'])
            # Get all products in one go
            items.extend(products.get_product(product_id) for product_id in contents)
        except (json.JSONDecodeError, KeyError):
            continue
    
    return items

def add_to_cart(username: str, product_id: int) -> None:
    dao.add_to_cart(username, product_id)

def remove_from_cart(username: str, product_id: int) -> None:
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str) -> None:
    dao.delete_cart(username)
    
    
    
    
import json

# import products
# from cart import dao
# from products import Product


# class Cart:
#     def __init__(self, id: int, username: str, contents: list[Product], cost: float):
#         self.id = id
#         self.username = username
#         self.contents = contents
#         self.cost = cost

#     def load(data):
#         return Cart(data['id'], data['username'], data['contents'], data['cost'])


# def get_cart(username: str) -> list:
#     cart_details = dao.get_cart(username)
#     if cart_details is None:
#         return []
    
#     items = []
#     for cart_detail in cart_details:
#         contents = cart_detail['contents']
#         evaluated_contents = eval(contents)  
#         for content in evaluated_contents:
#             items.append(content)
    
#     i2 = []
#     for i in items:
#         temp_product = products.get_product(i)
#         i2.append(temp_product)
#     return i2

    


# def add_to_cart(username: str, product_id: int):
#     dao.add_to_cart(username, product_id)


# def remove_from_cart(username: str, product_id: int):
#     dao.remove_from_cart(username, product_id)

# def delete_cart(username: str):
#     dao.delete_cart(username)