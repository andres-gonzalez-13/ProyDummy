from typing import Optional
from interfaces.UserRepository import UserRepository
from models.User import User

class DatabaseUserRepository(UserRepository):
    def get_user_by_email_and_password(self, email: str, password: str) -> Optional[User]:
        # Lógica para consultar el usuario por email y contraseña en la base de datos
        # y devolver el objeto User correspondiente, o None si no se encuentra
        user = User(1, "John Doe", "password123", "john.doe@example.com")
        return user