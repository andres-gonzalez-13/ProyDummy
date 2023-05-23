from interfaces.ProductInterface import ProductInterface
from typing import List
from models.Product import Product

class ProductService:
    def __init__(self, product_interface: ProductInterface):
        self.product_interface = product_interface

    def get_available_products(self) -> List[Product]:
        return self.product_interface.get_available_products()