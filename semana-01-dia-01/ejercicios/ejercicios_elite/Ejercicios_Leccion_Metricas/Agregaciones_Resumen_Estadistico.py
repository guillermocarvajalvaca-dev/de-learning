# Agregaciones y Resumen Estadistica para Daschboards
# 🎯 OBJETIVO RESUMIDO:
# • Operaciones: suma (+), división (/), resta (-), multiplicación (*)
# • Funciones: print(), f-strings, max(), min(), if/else anidado
# • Conceptos: agregación temporal, variación, crecimiento porcentual, insights automáticos
# • Patrón ETL: "Aggregation Layer" - resumir datos detallados para consumo ejecutivo

# 🧱 BLOQUES QUE CONSTRUYES:
# [BASE] Todas las operaciones previas → [NUEVO] Funciones de agregación (max/min) → [PRÓXIMO] Conexión a BI tools

# ============================================
# EJERCICIO 5: Agregación para Dashboard Ejecutivo
# ============================================
# Escenario: Tienes ventas diarias de una semana y necesitas
# generar un resumen con total, promedio, mejor día y variación.

# --- Ventas diarias simuladas (en miles de euros) ---
ventas_lunes = 12.5
ventas_martes = 18.3
ventas_miercoles = 15.7
ventas_jueves = 22.1
ventas_viernes = 31.4
ventas_sabado = 28.9
ventas_domingos = 19.2

# --- Cálculo del total semanal ---
# [OPERACIÓN: Suma acumulativa] Agregar valores discretos en una métrica consolidada
# [PATRÓN: Roll-up] Patrón fundamental en data warehousing: detalle → resumen
total_semanal = (ventas_lunes + ventas_martes + ventas_miercoles + ventas_jueves
                 + ventas_viernes + ventas_sabado + ventas_domingos)

# --- Cálculo del promedio diario ---
# [OPERACIÓN: División] Total / N días = valor representativo típico
# [CONCEPTO: Central Tendency] El promedio suaviza picos para análisis de tendencia
promedio_diario = total_semanal / 7

# --- Identificar el mejor día (máximo) ---
# [FUNCIÓN: max()] Encontrar el valor extremo en un conjunto
# [PATRÓN: Anomaly Detection] Los picos pueden indicar oportunidades o errores
mejor_venta = max(ventas_lunes, ventas_martes, ventas_miercoles,
                  ventas_jueves, ventas_viernes, ventas_sabado, ventas_domingos)

# --- Identificar el día con menor venta (mínimo) ---
# [FUNCIÓN: min()] Complemento de max() para rango completo de análisis
# [CONCEPTO: Baseline] Lo mínimo ayuda a establecer expectativas realistas
menor_venta = min(ventas_lunes, ventas_martes, ventas_miercoles, ventas_jueves,
                  ventas_viernes, ventas_sabado, ventas_domingos)

# --- Cálculo de la variación (rango) ---
# [OPERACIÓN: Resta] Máximo - Mínimo = dispersión de los datos
# [PATRÓN: Volatility Metric] Rango alto = mayor incertidumbre en planificación
variacion_semanal = mejor_venta - menor_venta

# --- Cálculo de crecimiento vs. promedio ---
# [OPERACIÓN: Fórmula de crecimiento %] ((Actual - Promedio) / Promedio) * 100
# [CONCEPTO: Trend Analysis] Comparar contra referencia para detectar dirección
crecimiento_vs_promedio = ((ventas_domingos - promedio_diario) / promedio_diario) * 100

# --- Salida formateada para dashboard ---
print("==== Resumen Ejecutivo Semanal ====")
print(f"Total semanal:  €{total_semanal:,.2f}K")
print(f"Promedio diario:  €{promedio_diario:.2f}K")
print(f"Mejor dia:  €{mejor_venta:,.2f}K")
print(f"Dia mas bajo:  €{menor_venta:,.2f}K")
print(f"Variacion (rango):  €{variacion_semanal:,.2f}K")
print(f"Domingo vs promedio: {crecimiento_vs_promedio:.1f}%")

# --- Insight automático para el reporte ---
# [PATRÓN: Automated Insights] Reglas simples que generan narrativas accionables
if crecimiento_vs_promedio > 10:
    print("Insight: Tendencia ALCISTA - Considerar aumentar inventario")
elif crecimiento_vs_promedio < 10:
    print("Insight: Tendencia BAJISTA - Revisar campanas de fin de semana")
else:
    print("Insight: Estabilidad - Mantener estrategia actual")


