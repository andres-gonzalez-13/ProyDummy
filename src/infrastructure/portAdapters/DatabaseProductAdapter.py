from typing import List
from infrastructure.interfaces.ProductInterface import ProductInterface
from domainBusines.Product import Product
from typing import Optional

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
    
    def create_product(self, id, name, price, units):

      # Crear un objeto cursor para ejecutar las consultas
      cursor = db.cursor()

      # Inserción del nuevo producto
      query = "INSERT INTO products (name, price, units) VALUES (%s, %s, %s)"
      values = (name, price, units)
      cursor.execute(query, values)

      db.commit()

      # Verificar si la inserción fue exitosa
      if cursor.lastrowid > 0:
          print("El nuevo producto se ha insertado correctamente.")
      else:
          print("No se pudo insertar el nuevo producto.")

      # Cerrar la conexión a la base de datos
      db.close()
    
    def get_product_by_id(self, id: int) -> Optional[Product]:
        prod = Product(0, 'cafe', 20, 100)
    
        return prod
