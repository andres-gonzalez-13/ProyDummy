from typing import List
from models.Product import Product

class ProductRepository:
    def get_available_products(self) -> List[Product]:
        raise NotImplementedError
