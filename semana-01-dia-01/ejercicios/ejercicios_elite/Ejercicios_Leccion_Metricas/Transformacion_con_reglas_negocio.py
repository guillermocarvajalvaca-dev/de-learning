# Objetivo: Aplicar cálculos de negocio sobre datos crudos (ej. conversión de moneda, impuestos).
from Curso_Autodidacta_basico_ED.ejercicios_elite.Ejercicios_Leccion_Metricas.Control_calidad_ingesta_datos import \
    umbral_Calidad_minimo

# ============================================
# EJERCICIO 4: Transformación de Datos con Reglas de Negocio
# ============================================
# Escenario: Recibes ventas en dólares y necesitas convertirlas a euros,
# aplicar impuestos locales y calcular el valor neto para reportes financieros.

# --- Datos crudos de una transacción ---
venta_bruta_usd = 1250.75  # Monto original en dólares
tasa_cambio_usd_eur = 0.92  # 1 USD = 0.92 EUR (valor simulado)
porcentaje_impuesto = 21  # IVA o impuesto local en porcentaje

# --- Paso 1: Conversión de moneda ---
# Multiplicamos por la tasa para obtener el valor en euros
venta_bruta_eur = venta_bruta_usd * tasa_cambio_usd_eur

# --- Paso 2: Cálculo del monto del impuesto ---
# Dividimos el porcentaje entre 100 para convertirlo a decimal, luego multiplicamos
monto_impuesto = venta_bruta_eur * (porcentaje_impuesto / 100)

# --- Paso 3: Cálculo del valor neto (lo que realmente ingresa) ---
# Restamos el impuesto del valor bruto
venta_neta_eur = venta_bruta_usd - monto_impuesto

# ---Paso 4: Calculo de margen si conocemos el costo---
costo_producto_eur = 680.00
margen_ganancia_eur = venta_neta_eur - costo_producto_eur
porcentaje_margen = (margen_ganancia_eur / venta_neta_eur) * 100

# --- Salida de transformación financiera ---
print("==== Transformacion Financiera de Venta ====")
print(f"Venta Original (USD): ${venta_bruta_usd:,.2f}")
print(f"Tasa Cambio: 1 USD = {tasa_cambio_usd_eur} EUR")
print(f"Venta bruta (EUR): {venta_bruta_eur:,.2f}")
print(f"Impuesto ({porcentaje_impuesto}%): €{venta_bruta_eur:,.2f}")
print(f" Venta neta (EUR): €{venta_neta_eur:,.2f})")
print(f"Margen de ganancia: €{margen_ganancia_eur:,.2f} ({porcentaje_margen:,.1f})")

# ---Regla de negocio Es una venta rentable?
umbral_margen_minimo = 30.0  # minimo aceptable: 30% margen
if porcentaje_margen >= umbral_Calidad_minimo:
    print("Decision: Venta RENTABLE - Aprobar para reporte")
else:
    print("Decision: Margen BAJO - Revisar estrategia de precios")
