# ============================================
# EJERCICIO 11: Generador de Insights Condicionales
# ============================================
# Escenario: Generar un mensaje de insight basado en el cumplimiento de la meta.
# Lógica: Reglas de negocio simples para narrativa automática.
# [PATRÓN: Automated Insights] Reglas simples que generan narrativas accionables.


def generate_performance_insights(actual: float, target: float) -> str:
    """
        Genera un mensaje de insight basado en el cumplimiento de la meta.

        Args:
            actual: Valor real alcanzado.
            target: Meta establecida.

        Returns:
            String con el mensaje de insight.
    """
    # [LÓGICA: If/Else Anidado] Clasificación de rendimiento
    if actual > target * 1.1:
        return "Insight: Tendencia ALCISTA - Supero meta en >10%"
    elif actual > target:
        return "Insight: Tendencia OPTIMA - Meta cumplida"
    elif actual > target * 0.8:
        return "Insight Atencion - Cerca del limite inferior (80%)"
    else:
        return "Insight: Critico - Por debajo del 80% de la meta"


if __name__ == "__main__":
    print(generate_performance_insights(85.0, 100.0))

# ============================================
# EJERCICIO 12: Transformación de Precios (List Comp)
# ============================================
# Escenario: Limpia strings de precio y aplica impuestos.
# Lógica: List comprehension para transformación masiva.
# [PATRÓN: Vectorization] Operación sobre toda la colección sin loop explícito.

from typing import List


def calculate_tax(prices: List[str], tax_rate: float = 0.16) -> List[float]:
    """
        Limpia strings de precio y aplica impuestos.

        Args:
            prices: Lista de precios como string con símbolo $.
            tax_rate: Tasa de impuesto a aplicar.

        Returns:
            Lista de precios finales como float.
    """
    # [OPERACIÓN: Replace + Float] Limpieza de string y casteo
    # [OPERACIÓN: Multiplicación] Aplicación de tasa impositiva
    return [float(p.replace('$', '')) * (1 + tax_rate) for p in prices]


if __name__ == '__main__':
    raw_price = ["$10.00", "$20.50", "$5.00"]
    print(calculate_tax(raw_price))

# ============================================
# EJERCICIO 13: Resumen Ejecutivo Estructurado
# ============================================
# Escenario: Genera un diccionario resumen con todos los KPIs clave.
# Lógica: Encapsular métricas en un objeto único.
# [PATRÓN: DTO (Data Transfer Object)] Estructura para pasar datos entre capas.

from typing import List, Dict


def create_executive_summary(sales: List[float]) -> Dict[str, float]:
    """
        Genera un diccionario resumen con todos los KPIs clave.

        Args:
            sales: Lista de ventas diarias.

        Returns:
            Diccionario con total, promedio, max, min.
    """
    if not sales:
        return {}
    # [OPERACIÓN: Construcción Dict] Empaquetado de múltiples métricas
    return {
        "Total": sum(sales),
        "average": sum(sales) / len(sales),
        "max": max(sales),
        "min": min(sales),
        "volatility": max(sales) - min(sales)
    }


if __name__ == '__main__':
    weekly_sales = [12.5, 18.3, 15.7, 22.1, 31.4, 28.9, 19.2]
    summary = create_executive_summary(weekly_sales)
    # En produccion, esto se enviaria como JSON a un dashboard
    print(summary)

# ============================================
# EJERCICIO 14: Generador de Chunks (Generator)
# ============================================
# Escenario: Generador eficiente de cuadrados.
# Lógica: Yield para no cargar todo en RAM.
# [PATRÓN: Lazy Evaluation] Calcular valores solo cuando se solicitan.

from typing import Generator


def square_generator(limit: int) -> Generator[int, None, None]:
    """
        Generador eficiente de cuadrados.

        Args:
            limit: Límite superior (exclusivo).

        Yields:
            El cuadrado del número actual.
    """
    # [OPERACIÓN: Yield] Pausa la función y retorna valor sin perder estado
    # [CONCEPTO: Memoria] Ideal para procesar millones de registros sin crash
    for i in range(limit):
        yield i ** 2


if __name__ == '__main__':
    gen = square_generator(15)
    print(list(gen))  # Consumir el generador

# ============================================
# EJERCICIO 15: Validación de Calidad de Datos
# ============================================
# Escenario: Valida que la lista de ventas no contenga valores negativos.
# Lógica: Check preventivo antes de procesamiento.
# [PATRÓN: Data Quality Gate] Bloquear datos sucios antes del pipeline.


from typing import List, Optional


def validate_sales_data(sales: List[float]) -> Optional[str]:
    """
        Valida que la lista de ventas no contenga valores negativos.

        Args:
            sales: Lista de ventas a validar.

        Returns:
            Mensaje de error si hay datos inválidos, None si es válido.
    """
    # [OPERACIÓN: any()] Verifica condición en toda la lista eficientemente
    if any(s < 0 for s in sales):
        return "Error de Calidad: Se detectaron ventas negativas."
    if not sales:
        return "Error de Calidad: Lista de ventas vacia"
    return None


if __name__ == '__main__':
    data_valid = [10.0, 20.0]
    data_invalid = [10.0, -05.0]

    error = validate_sales_data(data_valid)
    if error:
        print(error)
    else:
        print("Datos validados correctamente.")
