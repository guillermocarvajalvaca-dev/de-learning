# Objetivo: Dividir un dataset grande en batches manejables para procesamiento paralelo.

# ============================================
# EJERCICIO 3: Estrategia de Particionamiento de Datos
# ============================================
# Escenario: Tienes 125,000 registros y necesitas procesarlos en lotes
# de máximo 500 registros para no saturar la memoria.
# Debes calcular cuántos batches necesitas y manejar el "residuo".

# --- Configuración del volumen de datos ---
total_registros = 125000
tamano_maximo_batch = 500  # limite por razones de memoria/cpu

# --- Cálculo de batches completos ---
# División entera (//) nos dice cuántos batches de 500 caben exactamente
batches_completos = total_registros // tamano_maximo_batch

# --- Cálculo de batches completos ---
# División entera (//) nos dice cuántos batches de 500 caben exactamente
registros_restantes = total_registros - tamano_maximo_batch

# --- Cálculo del total real de batches ---
# Si hay residuo, necesitamos un batch adicional para los que sobran
# Usamos una condición simple: si hay resto, sumamos 1
total_batches = batches_completos + (1 if registros_restantes > 0 else 0)

# --- Cálculo del tamaño promedio por batch (para balanceo) ---
# Útil para distribuir carga equitativa en procesamiento paralelo
tamano_promedio_batch = total_registros / total_batches

# ---Salida de planificacion de particionamiento
print(f"===Plan de Particionamiento de Datos===")
print(f"Total registros: {total_registros:,}")
print(f"Tamano maximo batch: {tamano_maximo_batch:,}")
print(f"Batches completos: {batches_completos:,}")
print(f"Registros restantes: {registros_restantes:,}")
print(f"Total batches necesarios: {total_batches:,}")
print(f"Tamano promedio: {tamano_promedio_batch:,}")
