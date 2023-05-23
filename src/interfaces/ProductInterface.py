from typing import List
from models.Product import Product

class ProductInterface:
    def get_available_products(self) -> List[Product]:
        raise NotImplementedError
