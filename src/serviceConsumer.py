import requests

# URL base del microservicio
base_url = 'http://localhost:8083'  # Reemplaza "puerto" con el puerto en el que se ejecuta tu microservicio

# Crear un producto
create_product_url = base_url + '/product'
payload = {
    'id': 10,
    'code': '11111',
    'name': 'cafe',
    'price': 15.0
}
response = requests.post(create_product_url, json=payload)

if response.status_code == 200:
    print('Producto creado exitosamente')
else:
    print('Error al crear el producto:', response.text)

# Consultar productos
get_products_url = base_url + '/product'
response = requests.get(get_products_url)

if response.status_code == 200:
    products = response.json()
    print('Productos disponibles:')
    for product in products:
        print('ID:', product['id'])
        print('code:', product['code'])
        print('name:', product['name'])
        print('price:', product['price'])
        print('---')
else:
    print('Error al consultar los productos:', response.text)

# Borrar un producto
product_id = 1  # ID del producto a borrar
delete_product_url = base_url + '/product/{}'.format(product_id)
response = requests.delete(delete_product_url)

if response.status_code == 200:
    print('Producto borrado exitosamente')
else:
    print('Error al borrar el producto:', response.text)
