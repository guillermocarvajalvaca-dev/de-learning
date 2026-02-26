"""
EJERCICIO 1: Métricas de Pipeline ETL
Objetivo: Calcular estadísticas básicas de un proceso ETL
"""

# Datos de entrada (simulando registros procesados)
registros_origen = 15420
registros_destino = 15385
tiempo_procesamiento_segundos = 245

# TODO: Calcula:
# 1. Registros perdidos (diferencias)
# 2. Porcentaje de exitos
# 3. Tiempo promedio por registro (en milisegundos)

# Escribe tu codigo aqui:
registros_perdidos = registros_origen - registros_destino
porcentaje_exitos = (registros_origen + registros_destino) * 100
tiempo_ms_por_registro = (tiempo_procesamiento_segundos * 1000) / registros_destino

print(f"====Metricas del Pipeline ETL===")
print(f"Registro origen: {registros_origen: ,}")
print(f"Resgistro destino: {registros_destino: ,}")
print(f"Registros perdidos: {registros_perdidos: ,}")
print(f"porcentaje exitos: {porcentaje_exitos: ,}")
print(f"Tiempo por registro: {tiempo_ms_por_registro: ,}")
