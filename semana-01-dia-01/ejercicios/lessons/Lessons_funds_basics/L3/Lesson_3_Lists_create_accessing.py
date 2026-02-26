# Creando y accediendo a listas
# Lista de registros de ventas (simulando datos de una base de datos)
ventas_diarias = [1500, 2300, 1890, 2100, 1750, 3200, 2800]

# acceder por indice (posicion)
print(f"Ventas lunes: {ventas_diarias[0]}")  # Primer elemento
print(f"Ventas_viernes: {ventas_diarias[4]}")  # Segundo elemento
print(f"Ventas_domingos: {ventas_diarias[-1]}")  # ultimo elemento

# Longitud
total_dias = len(ventas_diarias)
print(f"Total de dias: {total_dias}")
