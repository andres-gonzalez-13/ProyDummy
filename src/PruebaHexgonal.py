from infrastructure.portAdapters.DatabaseUsersAdapter import DatabaseUserAdapter
from infrastructure.services.UserService import UserService

from infrastructure.portAdapters.DatabaseProductAdapter import DatabaseProductAdapter
from infrastructure.services.ProductService import ProductService

user_adapter = DatabaseUserAdapter()
user_service = UserService(user_adapter)

user = user_service.get_user_by_email_and_password("johndoe@example.com", "password123")
#user = user_service.get_user_by_email_and_password("andres.gonzalez04@uptc.edu.co", "mimimimi")

if user is None:
    print("no existe el usuario")
else:
    print("Nombre del usuario: " + user.name)

#---------------------------------

prod_adapter = DatabaseProductAdapter()
prod_service = ProductService(prod_adapter)

listProd = prod_service.get_available_products()

for prod in listProd:
    print(prod.name)

#------------------------

user_adapter = DatabaseUserAdapter()
user_service = UserService(user_adapter)

#user = user_service.create_user('1', 'mafe', 'correee', 'mafe@gmail.com')
#user = user_service.get_user_by_email_and_password("andres.gonzalez04@uptc.edu.co", "mimimimi")

if user is None:
    print("no existe el usuario")
else:
    print("Nombre del usuario: " + user.name)

prod_service.create_product("1", "cafe", 20.0, 100)