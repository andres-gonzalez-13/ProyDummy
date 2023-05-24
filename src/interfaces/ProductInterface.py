from typing import List
from models.Product import Product

class ProductInterface:
    def get_available_products(self) -> List[Product]:
        raise NotImplementedError
    
    def create_product(self, id: str, name: str, price: float, units: int):
        raise NotImplementedError
