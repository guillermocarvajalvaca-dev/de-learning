# Datos de un mes (30 días)
registros_mes = list(range(100, 3100, 100))  # 100, 200, 300... 3000

# slicing: [inicio:fin:paso]
primeros_7 = registros_mes[:7]  # dias 1 - 7
ultimos_7 = registros_mes[-7:]  # Ultimos 7 dias
cada_5_dias = registros_mes[:5]  # Muestreo cada 5 dias

print(f"Primeros 7 dias: {primeros_7}")
print(f"Ultimos 7 dias: {ultimos_7}")
print(f"Muestreo cada 5 dias: {cada_5_dias}")
