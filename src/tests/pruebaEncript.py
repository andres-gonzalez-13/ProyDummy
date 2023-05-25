
import bcrypt

def encriptar_password(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password

def verificar_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)

# Ejemplo de uso
password = "mi_contraseña"

# Encriptar la contraseña
hashed_password = encriptar_password(password)
print("Contraseña encriptada:", hashed_password.decode())

# Verificar la contraseña
password_verificado = input("Ingrese la contraseña a verificar: ")
verificado = verificar_password(password_verificado, hashed_password)

if verificado:
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")