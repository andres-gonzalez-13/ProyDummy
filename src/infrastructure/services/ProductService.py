from infrastructure.interfaces.ProductInterface import ProductInterface
from typing import List
from domainBusines.Product import Product
from typing import Optional

class ProductService:
    def __init__(self, product_interface: ProductInterface):
        self.product_interface = product_interface

    def get_available_products(self) -> List[Product]:
        return self.product_interface.get_available_products()
    
    def create_product(self, id: str, name: str, price: float, units: int):
        return self.product_interface.create_product(id, name, price, units)
    
    def get_product_by_id(self, id: int) -> Optional[Product]:
        return self.product_interface.get_product_by_id(id)