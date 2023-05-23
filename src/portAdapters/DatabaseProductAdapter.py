from typing import List
from interfaces.ProductInterface import ProductInterface
from models.Product import Product

import mysql.connector

# Conectarse a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mimimimi",
  database="ahorcado"
)



class DatabaseProductAdapter(ProductInterface):
    def get_available_products(self) -> List[Product]:        
        products = []

        cursor = db.cursor()

        # Consulta de todos los productos disponibles
        query = "SELECT * FROM products"
        cursor.execute(query)

        # Obtener los resultados
        results = cursor.fetchall()

        # Verificar si se encontraron productos
        if results:
            print("Productos disponibles:")
            for result in results:
                producto1 = Product(result[0], result[1], result[2], result[3])
                products.append(producto1)

        producto2 = Product(2, "Pantalón", 39.99, 5)
        products.append(producto2)

        producto3 = Product(3, "Zapatos", 59.99, 3)
        products.append(producto3)

        return products
