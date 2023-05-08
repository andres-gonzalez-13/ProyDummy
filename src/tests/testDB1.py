import mysql.connector

# Conectarse a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mimimimi",
  database="ahorcado"
)

# Crear un objeto cursor para ejecutar las consultas
cursor = db.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM word")

# Obtener los resultados
results = cursor.fetchall()

# Imprimir los resultados
for result in results:
  print(result)

# Cerrar la conexión a la base de datos
db.close()
