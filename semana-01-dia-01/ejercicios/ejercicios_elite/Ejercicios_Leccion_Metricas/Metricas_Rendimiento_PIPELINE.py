# 🎯 OBJETIVO RESUMIDO:
# • Operaciones: resta (-), división (/), multiplicación (*)
# • Funciones: print(), f-strings, if/else, cálculos con timestamps
# • Conceptos: throughput, latencia, SLA, proyección temporal
# • Patrón ETL: "Performance Monitoring" - métricas de rendimiento en tiempo real

# 🧱 BLOQUES QUE CONSTRUYES:
# [BASE] Resta y división del Ej.1 → [NUEVO] Timestamps y proyecciones → [PRÓXIMO] Alertas automáticas

# ============================================
# EJERCICIO 2: Métricas de Rendimiento de Pipeline
# ============================================
# Escenario: Tu pipeline procesa datos cada hora.
# Necesitas saber qué tan rápido trabaja y si cumple con los SLA.

# ----Datos de ejecucion del ultimo batch ---
registros_procesados = 45000
tiempo_inicio_segundos = 170000000  # Timestamp Unix: segundos desde 1970-01-01
tiempo_fin_segundos = 1700000245  # Mismo formato para consistencia

# --- Calculo del tiempo total del procesamiento ---
# [OPERACION: Resta de timestamps] Diferencias - duracion real en segundos
# [CONCEPTO: Elapsed Time] Metrica fundamental para cualquier sistema distribuido
duracion_total_segundos = tiempo_fin_segundos - tiempo_inicio_segundos

# --- Cálculo de throughput: registros por segundo ---
# [OPERACIÓN: División] Total / Tiempo = Velocidad de procesamiento
# [PATRÓN: Scalability Metric] Esta cifra determina si necesitas más recursos
throughput_registros_por_segundo = registros_procesados / duracion_total_segundos

# --- Cálculo de latencia promedio por registro (en milisegundos) ---
# [OPERACIÓN: Conversión de unidades] *1000 para segundos→milisegundos
# [CONCEPTO: User Experience] Latencia alta = usuarios perciben lentitud
latencia_promedio_ms = (duracion_total_segundos * 1000) / registros_procesados

# --- Proyección: ¿Cuántos registros procesaría en 1 hora? ---
# [OPERACIÓN: Multiplicación] Throughput * 3600s = capacidad horaria estimada
# [PATRÓN: Capacity Planning] Útil para dimensionar infraestructura futura
proyeccion_hora = throughput_registros_por_segundo * 3600

# ---Salida de metricas de rendimiento ---
print("==== Metricas de Rendimiento del Pipeline ====")
print(f"Registros procesados: {registros_procesados:,}")
print(f"Duracion Total: {duracion_total_segundos:,}")
print(f"throughput registros: {throughput_registros_por_segundo:.2f} registros/segundo")
print(f"Latencia promedio: {latencia_promedio_ms:.2f} ms por registro")
print(f"Proyeccion: {proyeccion_hora:,.0f} registros")

# --- Validación contra SLA ---
# [PATRÓN: SLO Enforcement] Comparar métricas reales vs. acuerdos de servicio
sla_throughput_minimo = 150  # minimo aceptable: 150 registros/segundo
if throughput_registros_por_segundo >= sla_throughput_minimo:
    print("SLA: CUMPLIDO - Rendimiento dentro de lo esperado")
else:
    print("SLA: INCUMPLIDO - Revisar Optimizaciones")
