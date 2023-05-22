from typing import Optional
from interfaces.UserRepository import UserRepository
from models.User import User

import mysql.connector

# Conectarse a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mimimimi",
  database="ahorcado"
)

class DatabaseUserRepository(UserRepository):
    def get_user_by_email_and_password(self, email: str, password: str) -> Optional[User]:
        # Lógica para consultar el usuario por email y contraseña en la base de datos
        # y devolver el objeto User correspondiente, o None si no se encuentra
        user = User(1, "John Doe", "password123", "john.doe@example.com")
        #user = User(2, 'santi', password, email)
        

        if email == "":
            user = None
        else:
            cursor = db.cursor()
            # Ejecutar una consulta
            query = "SELECT * FROM user WHERE email = %s"
            cursor.execute(query, (email,))
            # Obtener los resultados
            result = cursor.fetchone()
            if result:
                user = User(result[0],result[1],result[2],result[3])
            else:
                user = None
        return user