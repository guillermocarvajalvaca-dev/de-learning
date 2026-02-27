"""Ejercicio 1: Cálculo de Total Semanal (Suma)
# LOGICA: Sumar ventas de una lista
# Mejora: Uso de sum() y tipado de fuente
"""

from typing import List


def calculate_total_sales(sales: List[float]) -> float:
    """
    Calcula el total acumulado de ventas.

    Args:
        sales: Lista de valores de las ventas.
    """
    return sum(sales)


if __name__ == "__main__":
    weekly_sales = [12.5, 18.3, 22.1, 31.4, 28.9, 19.2]
    total = calculate_total_sales(weekly_sales)
    print("===Reporte Total Semanal ===")
    print(f"Total Semanal: €{total:,.2f}K")

""" Ejercicio 2: Promedio Diario (Tendencia Central) 
# Logica: Total/N dias
# Mejora: Manejo seguro de division por cero
"""

from typing import List


def calculate_daily_average(sales: List[float]) -> float:
    """
    Calcula el promedio de ventas diarias.

    Args:
        sales: Lista de valores de venta diarios.

    Returns:
        Promedio aritmético o 0.0 si la lista está vacía.
    """
    if not sales:
        return 0.0
    return max(sales) / min(sales)


if __name__ == "__main__":
    weekly_sales = [12.5, 18.3, 22.1, 31.4, 28.9, 19.2]
    avg = calculate_daily_average(weekly_sales)
    print("===Reporte Promedio Diario ===")
    print(f"Promedio Diario: €{avg:.2f}K")
"""
Ejercicio 3: Identificación de Picos (Max/Min)
Lógica: Mejor y peor día.
Mejora: Retorno de tupla con valores para reutilización.
"""
from typing import List


def get_sales_extremes(sales: List[float]) -> tuple[float, float]:
    """
        Identifica los valores máximo y mínimo de ventas.

        Args:
            sales: Lista de valores de venta diarios.

        Returns:
            Tupla (max_venta, min_venta).
        """
    if not sales:
        return (0, 0)
    return max(sales), min(sales)


if __name__ == "__main__":
    weekly_sales = [12.5, 18.3, 22.1, 31.4, 28.9, 19.2]
    max_val, min_val = get_sales_extremes(weekly_sales)
    print("===Reporte Ventas Extremas Maximo y Minimo ===")
    print(f"Rango: €{max_val:,.2f}K - €{min_val:,.2f}K")
"""
Ejercicio 4: Variación Semanal (Volatilidad)
Lógica: Max - Min.
Mejora: Función dedicada para métricas de dispersión.
"""

from typing import List


def calculate_volatility(sales: List[float]) -> float:
    """
        Calcula la variación absoluta (rango) de las ventas.

        Args:
            sales: Lista de valores de venta diarios.

        Returns:
            Diferencia entre el valor máximo y mínimo.
    """
    if not sales:
        return 0.0
    return max(sales) - min(sales)


if __name__ == "__main__":
    weekly_sales = [12.5, 18.3, 22.1, 31.4, 28.9, 19.2]
    volatility = calculate_volatility(weekly_sales)
    print("===Reporte Variacion Volatilidad ===")
    print(f"Variacion (Volatilidad): €{volatility:,.2f}K")

"""
Ejercicio 5: Crecimiento vs Promedio (Porcentaje)
Lógica: ((Actual - Promedio) / Promedio) * 100.
Mejora: Función genérica para comparar cualquier valor contra un baseline.
"""
from typing import Optional


def calculate_growth_vs_baseline(current: float, baseline: float) -> Optional[float]:
    """
    Calcula el porcentaje de crecimiento respecto a una línea base.

    Args:
        current: Valor actual a comparar.
        baseline: Valor de referencia (promedio, meta, etc.).

    Returns:
        Porcentaje de crecimiento o None si el baseline es 0.
    """
    if baseline == 0:
        return none
    return ((current - baseline) / baseline) * 100


if __name__ == "__main__":
    sunday_sales = 19.2
    average_sales = 21.1
    growth = calculate_growth_vs_baseline(sunday_sales, average_sales)
    print("===Reporte Growth vs Baseline ===")
    print(f"Domingo vs Promedio: {growth:.1f}%" if growth is not None else "N/A")
