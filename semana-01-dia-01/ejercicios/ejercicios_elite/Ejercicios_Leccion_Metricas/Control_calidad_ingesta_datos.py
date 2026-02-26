# ============================================
# EJERCICIO 1: Calidad de Datos en Ingesta
# ============================================
# Escenario: Acabas de recibir un archivo CSV con 10,000 registros.
# Necesitas validar cuántos están completos, cuántos tienen errores
# y qué porcentaje puedes procesar con confianza.

# --- Datos simulados del lote recibido ---
total_registros_recibidos = 10000
registros_con_nulls = 245  # Filas con valores faltantes criticos
registros_con_formato_invalidos = 89  # filas con fechas o numeros mal escritos
registros_duplicados = 34  # filas repetidas que deben eliminarse

# -----"Calculo de registros limpios" y listos para procesar ---
# Restamos todos los problemas para obtener solo los registros validos
registros_validos = total_registros_recibidos - registros_con_nulls - registros_con_formato_invalidos

# ---Calculo del porcentaje de calidad ---
# Dividimos los validos entre el total y multiplicamos por 100 para obtener porcentaje
porcentaje_calidad = (registros_validos / total_registros_recibidos) * 100

# ---Calculo de registros a rechazar ---
# Ultimo para generar reportes de auditoria o reintentos
registros_a_rechazar = total_registros_recibidos - registros_validos

# --- Salida de metricas para monitoreo ---
print("===Reporte de Calidad de Ingesta===")
print(f"Total recibidos: {total_registros_recibidos}")
print(f"Registros Validos: {registros_validos}")
print(f"Registros a rechazar: {registros_a_rechazar}")
print(f"Porcentaje de calidad: {porcentaje_calidad:.2f}%")

# --- Regla de Negocio:Podemos continuar con pipeline? ---
# En produccion, definimos un umbral minimo de calidad (ej.95%)
umbral_Calidad_minimo = 95.0
if porcentaje_calidad >= umbral_Calidad_minimo:
    print("Pipeline: CONTINUAR - Calidad aceptable")
else:
    print("Pipeline: DETENER - Calidad Insuficiente")
