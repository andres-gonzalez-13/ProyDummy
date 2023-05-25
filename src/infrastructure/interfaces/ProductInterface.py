from typing import List
from typing import Optional
from domainBusines.Product import Product

class ProductInterface:
    def get_available_products(self) -> List[Product]:
        raise NotImplementedError
    
    def create_product(self, id: str, name: str, price: float, units: int):
        raise NotImplementedError
    
    def get_product_by_id(self, id: int) -> Optional[Product]:
        raise NotImplementedError
