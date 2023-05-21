from interfaces.ProductRepository import ProductRepository
from typing import List
from models.Product import Product

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_available_products(self) -> List[Product]:
        return self.product_repository.get_available_products()