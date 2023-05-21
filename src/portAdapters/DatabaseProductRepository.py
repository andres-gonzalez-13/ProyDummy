from typing import List
from interfaces.ProductRepository import ProductRepository
from models.Product import Product

class DatabaseProductRepository(ProductRepository):
    def get_available_products(self) -> List[Product]:        
        products = []

        producto1 = Product(1, "Camisa", 29.99, 10)
        products.append(producto1)

        producto2 = Product(2, "Pantalón", 39.99, 5)
        products.append(producto2)

        producto3 = Product(3, "Zapatos", 59.99, 3)
        products.append(producto3)

        return products
