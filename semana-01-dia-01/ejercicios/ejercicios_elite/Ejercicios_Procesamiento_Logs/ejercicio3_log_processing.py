"""
EJERCICIO 3: Procesamiento de Logs de Servidor
Simulando análisis de logs de un pipeline de datos
"""

# Logs de ejecucion (timestamp, status, registros_procesados)

logs = [
    "2024-02-20 10:00:00,SUCCESS,1500",
    "2024-02-20 10:15:00,FAILED,0",
    "2024-02-20 10:30:00,SUCCESS,2300",
    "2024-02-20 10:45:00,SUCCESS,1890",
    "2024-02-20 11:00:00,FAILED,0 ",
    "2024-02-20 11:15:00,SUCCESS,3200",
    "2024-02-20 11:30:00,SUCCESS,2800 ",
]

# SOLUCION
jobs_exitosos = []
registros_exitosos = []

for log in logs:
    partes = log.split(",")
    status = partes[1]
    registros = int(partes[2])

    if status == "SUCCESS":
        jobs_exitosos.append(log)
        registros_exitosos.append(registros)

total_registros = sum(registros_exitosos)
max_registros = max(registros_exitosos)
promedio = total_registros / len(registros_exitosos)

print(f"=== Analisis de logs ====")
print(f"Jobs Exitosos: {len(jobs_exitosos)}")
print(f"Total registros procesados: {total_registros:,}")
print(f"Job con mas registros: {max_registros:,}")
print(f"Promedio por job: {promedio:.2f}")
print(f"\nJobs exitosos:")
for job in jobs_exitosos:
    print(f" - {job}")
