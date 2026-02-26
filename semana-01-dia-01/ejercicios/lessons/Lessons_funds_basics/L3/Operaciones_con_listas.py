# Operaciones con Listas en Data Engineering

# Sumar listas (concatenar batches)
batch_1 = [100, 200, 300]
batch_2 = [400, 500, 600]
batch_completo = batch_1 + batch_2
print(f"Batch completo: {batch_completo}")

# Funciones agregadas (estadisticas basicas)
temperaturas = [22.5, 23.0, 21.8, 24.2, 22.1]

print(f"Temperatura maxima: {max(temperaturas)}")
print(f"Temperatura minima: {min(temperaturas)}")
print(f"Suma total: {sum(temperaturas)}")
print(f"Promedio: {sum(temperaturas) / len(temperaturas):.2f}")

# Ordenar datos
temperaturas_ordenadas = sorted(temperaturas)
print(f"Ordenadas: {temperaturas_ordenadas}")

# Orden descendente
temperaturas_desc = sorted(temperaturas, reverse=True)
print(f"Descendente: {temperaturas_desc}")
