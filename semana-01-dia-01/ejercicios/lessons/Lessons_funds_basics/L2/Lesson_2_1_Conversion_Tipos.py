# Datos crudos vienen como strings desde archivos/APIs
dato_crudo = "15420"

# Convertir a entero para operaciones matematicas
ventas = int(dato_crudo)
print(f"Ventas + 100: {ventas + 100}")

# Convertir a float para decimales
precio_str = "19.99"
precio = float(precio_str)
print(f"Precio con IVA: {precio * 1.16}")

# Convertir a string para concatenar el logs
transacciones = 1500
mensaje = "Total de transacciones: " + str(transacciones)
print(mensaje)

# Booleanos - utiles para filtros
usuarios_activos = 150
tiene_usuarios = bool(usuarios_activos)  # True si > 0
print(f"Tienes usuarios activos? {tiene_usuarios}")
