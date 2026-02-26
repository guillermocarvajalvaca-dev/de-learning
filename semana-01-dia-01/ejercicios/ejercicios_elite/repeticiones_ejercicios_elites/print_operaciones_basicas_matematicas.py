# CONCEPTO 1: print() y Operaciones Matemáticas
# Ejercicio E1.1-G: Calculadora de ROI para campaña de marketing
# Contexto: Un Data Engineer necesita calcular el retorno de inversión de pipelines de datos+

inversion_pipeline = 50000  # USD
ahorro_automatizacion = 120000  # USD anual
tiempo_meses = 12

roi_porcentaje = ((ahorro_automatizacion - inversion_pipeline) / inversion_pipeline) * 100
roi_mensual = roi_porcentaje / tiempo_meses

print(f"ROI Total: {roi_porcentaje:.2f}%")
print(f"Roi Mensual: {roi_mensual:.2f}%")
print(f"Payback period: {inversion_pipeline / (ahorro_automatizacion / 12):.1f} meses")

# NIVEL 2: Ejercicio Guiado (Carga media)
# Ejercicio E1.2-G: Métricas de calidad de datos
# Un pipeline procesó 1,000,000 de registros. Completa el código.

total_registros = 1000000
registros_validos = 985420
registros_nulos = 8500
registros_duplicados = 6080

# TODO: Calcula el porcentaje de calidad de datos
# Fórmula: (registros_validos / total_registros) * 100
porcentaje_calidad = (registros_validos / total_registros) * 100

# TODO: Calcula registros perdidos (nulos + duplicados)
perdida_total = (registros_nulos + registros_duplicados)

# TODO: Imprime un reporte con 2 decimales
print("=== Reporte Ejericio Carga Media ===")
print(f"Calidad de datos: {porcentaje_calidad:.2f}%")
print(f"Registros perdidos: {perdida_total:.2f}")

# NIVEL 3: Independiente (Carga alta)
# Ejercicio E1.3-I: Dimensionamiento de cluster
# Necesitas calcular recursos para un cluster de Spark

ram_por_nodo_gb = 64
num_nodos = 12
replicacion_factor = 3
overhead_porcentaje = 15

# Calcula:
# 1. RAM total del cluster
# 2. RAM usable (restando overhead)
# 3. Capacidad efectiva considerando replicación

# Escribe tu código aquí (5 líneas mínimo):
ram_total = ram_por_nodo_gb * num_nodos
overhead_gb = ram_total * (overhead_porcentaje / 100)
ram_usable = ram_total - overhead_gb
capacidad_efectiva = ram_usable / replicacion_factor
print("=== Reporte Dimensionamiento de Clusters ===")
print(f"1. RAM Total: {ram_total:.2f}GB")
print(f"2. RAM Usable: {ram_usable:.2f}GB")
print(f"3. Capacidad Efectiva: {capacidad_efectiva}")
