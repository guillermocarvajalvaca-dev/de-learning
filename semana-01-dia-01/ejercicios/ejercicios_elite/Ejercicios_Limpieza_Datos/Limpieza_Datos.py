"""
EJERCICIO 2: Limpieza de Datos Crudos
Simulando datos de una API o archivo CSV
"""

# Datos "sucios" como vienen de una fuente externa
datos_crudos = {
    "id_usuario": "15420",  # string, deberia ser int
    "nombre": " juan perez ",  # Con espacios
    "salario": "45000.50",  # string, deberia ser float
    "activo": "1",  # string deberia ser bool
    "edad": "28"  # string, deberia ser int
}

# TODO: Limpia y convierte los datos:
# 1. Convierte id_usuario a int
id_usuario = int(datos_crudos["id_usuario"])
# 2. Limpia espacios del nombre y capitaliza
nombre = datos_crudos["nombre"].strip().title()
# 3. Convierte salario a float
salario = float(datos_crudos["salario"])
# 4. Convierte activo a bool (1=True, 0=False)
activo = datos_crudos["activo"] == "1"
# 5. Convierte edad a int
edad = int(datos_crudos["edad"])

print(f"ID: {id_usuario} ({type(id_usuario).__name__})")
print(f"Nombre: '{nombre}' ({type(nombre).__name__})")
print(f"Salario: ${salario:,.2f} ({type(salario).__name__})")
print(f"Edad: {edad} ({type(edad).__name__})")
