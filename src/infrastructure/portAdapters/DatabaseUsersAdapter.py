from typing import Optional
from infrastructure.interfaces.UserInterface import UserInterface
from domainBusines.User import User

import mysql.connector

# Conectarse a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mimimimi",
  database="ahorcado"
)

class DatabaseUserAdapter(UserInterface):
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
            query = "SELECT * FROM user WHERE email = %s AND password = %s"

            values = (email, password)
            cursor.execute(query, values)
            # Obtener los resultados
            result = cursor.fetchone()
            if result:
                user = User(result[0],result[1],result[2],result[3])
            else:
                user = None
        return user
    
    def create_user(self, id: str, name: str, password: str, email: str) -> User:
        user = User(id,name,password,email)
        cursor = db.cursor()
        query = "INSERT INTO user (name, password, email) VALUES (%s, %s, %s)"
        values = (name, password, email)
        cursor.execute(query, values)

        db.commit()

        if cursor.lastrowid > 0:
            print("El nuevo usuario se ha insertado correctamente. ID:", cursor.lastrowid)
        else:
            print("No se pudo insertar el nuevo usuario.")

        # Cerrar la conexión a la base de datos
        db.close()
        return user