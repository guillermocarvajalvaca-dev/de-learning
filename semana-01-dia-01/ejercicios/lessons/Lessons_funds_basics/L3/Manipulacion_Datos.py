"""Manipulación de Listas para ETL"""

# Lista de registros de ventas (simulando datos de una base de datos)
ventas_diarias = [1500, 2300, 1890, 2100, 1750, 3200, 2800]

# Agregar datos al final (append)
ventas_diarias.append(3100)  # Agrega Lunes de la siguiente semana
print(f"Ventas_actualizadas:")

# Insertar en posicion especifica
ventas_diarias.insert(0, 1200)  # Insertar el inicio
print(f"Con dato faltante agregado: {ventas_diarias}")

# Eliminar por valor (remove)
ventas_diarias.remove(1200)  # elimina el valor 1200
print(f"Sin el dato faltante: {ventas_diarias}")

# eliminar por indice (pop)
ultimo_dato = ventas_diarias.pop()  # elimina y retorna el ultimop
print(f"Eliminado: {ultimo_dato}")
print(f"lista Final: {ventas_diarias}")
