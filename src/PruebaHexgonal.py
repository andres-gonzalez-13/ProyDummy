from portAdapters.DatabaseUsersRepository import DatabaseUserRepository
from services.UserService import UserService

user_repository = DatabaseUserRepository()
user_service = UserService(user_repository)

#user = user_service.get_user_by_email_and_password("johndoe@example.com", "password123")
user = user_service.get_user_by_email_and_password("andres.gonzalez04@uptc.edu.co", "mimimimi")

if user is None:
    print("no existe el usuario")
else:
    print("Nombre del usuario: " + user.name)