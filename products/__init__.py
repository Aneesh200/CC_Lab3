from products import dao
from functools import lru_cache
from typing import List

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> List[Product]:
    """List all products using list comprehension for better performance."""
    return [Product.load(product) for product in dao.list_products()]

@lru_cache(maxsize=128)
def get_product(product_id: int) -> Product:
    """Get a single product with caching for repeated lookups."""
    return Product.load(dao.get_product(product_id))

def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)

#from products import dao


#class Product:
    #def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        #self.id = id
        #self.name = name
        #self.description = description
        #self.cost = cost
        #self.qty = qty

    #def load(data):
        #return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


#def list_products() -> list[Product]:
    #products = dao.list_products()
    #result = []
    #for product in products:
        #result.append(Product.load(product))
    
    #return result



#def get_product(product_id: int) -> Product:
    #return Product.load(dao.get_product(product_id))


#def add_product(product: dict):
    #dao.add_product(product)


#def update_qty(product_id: int, qty: int):
    #if qty < 0:
        #raise ValueError('Quantity cannot be negative')
    #dao.update_qty(product_id, qty)
