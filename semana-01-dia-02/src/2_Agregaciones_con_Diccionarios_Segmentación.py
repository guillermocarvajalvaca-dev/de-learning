"""
Enfoque: Agrupar datos por categorías (Región, Producto)
para dashboards multidimensionales.
Ejercicio 6: Ventas por Categoría (Agrupación)
Lógica: Sumar ventas agrupadas por nombre de categoría.
Mejora: Uso de dict.get() para acumulación segura.
"""
from typing import List, Dict, Any


def aggregate_sales_by_category(transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
        Agrupa el total de ventas por categoría de producto.

        Args:
            transactions: Lista de diccionarios con 'categoria' y 'monto'.

        Returns:
            Diccionario {categoria: total_ventas}.
    """
    aggregated = {}
    for transaction in transactions:
        category = transaction['categoria']
        amount = transaction['monto']
        aggregated[category] = aggregated.get(category, 0.0) + amount
    return aggregated


if __name__ == '__main__':
    data = [
        {'categoria': 'Electronica', 'monto': 100.0},
        {'categoria': 'Hogar', 'monto': 50.0},
        {'categoria': 'Electronica', 'monto': 200.0}
    ]
    print(aggregate_sales_by_category(data))

"""
Ejercicio 7: Conteo de Transacciones por Región
Lógica: Contar cuántas ventas hubo por región.
Mejora: Separación de conteo vs suma monetaria.
"""
from typing import List, Dict, Any


def count_transactions_by_region(transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
        Cuenta el número de transacciones por región.

        Args:
            transactions: Lista de diccionarios con 'region'.

        Returns:
            Diccionario {region: cantidad_transacciones}.
    """
    counts = {}
    for transaction in transactions:
        region = transaction['region']
        counts[region] = counts.get(region, 0) + 1
    return counts


if __name__ == '__main__':
    data = [
        {'region': 'Norte'}, {'region': 'Sur'}, {'region': 'Norte'}
    ]
    print(count_transactions_by_region(data))
"""
Ejercicio 8: Ticket Promedio por Vendedor
Lógica: Total Ventas Vendedor / Total Transacciones Vendedor.
Mejora: Cálculo compuesto en dos pasos (suma y conteo).
"""

from typing import List, Dict, Any


def calculate_avg_ticket_per_seller(transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
        Calcula el ticket promedio por vendedor.

        Args:
            transactions: Lista con 'vendedor' y 'monto'.

        Returns:
            Diccionario {vendedor: ticket_promedio}.
    """
    totals = {}
    counts = {}

    for t in transactions:
        seller = t['vendedor']
        amount = t['monto']
        totals[seller] = totals.get(seller, 0.0) + amount
        counts[seller] = counts.get(seller, 0) + 1
    return {seller: totals[seller] / counts[seller] for seller in totals}


if __name__ == '__main__':
    data = [
        {'vendedor': 'Ana', 'monto': 100}, {'vendedor': 'Ana', 'monto': 200},
        {'vendedor': 'Luis', 'monto': 50}
    ]
    print(calculate_avg_ticket_per_seller(data))

"""
Ejercicio 9: Filtrado de Datos para Dashboard (List Comprehension)
Lógica: Mostrar solo ventas mayores a un umbral.
Mejora: Uso de List Comprehension para eficiencia y legibilidad.
"""

from typing import List, Dict, Any


def filter_high_value_transactions(transactions: List[Dict[str, Any]], threshold: float) -> List[Dict[str, Any]]:
    """
    Filtra transacciones superiores a un umbral determinado.

    Args:
        transactions: Lista de transacciones.
        threshold: Valor mínimo para considerar 'alta valor'.

    Returns:
        Lista filtrada de transacciones.
    """
    return [t for t in transactions if t['monto'] > threshold]


if __name__ == '__main__':
    data = [
        {'id': 1, 'monto': 50}, {'id': 2, 'monto': 150}, {'id': 3, 'monto': 200}
    ]
    print(filter_high_value_transactions(data, 100.0))
print(f"✅ Progreso Día 2: {10}/15 ejercicios completados ({(10 / 15) * 100:.0f}%)")

"""
Ejercicio 10: Extracción de Keys para Gráficos (Dict Keys)
Lógica: Obtener etiquetas (labels) para un gráfico de barras.
Mejora: Conversión explícita de vistas de diccionario a listas.
"""

from typing import Dict, List


def extract_chart_labels(data: Dict[str, float]) -> List[str]:
    """
    Extrae las claves de un diccionario para usar como etiquetas en gráficos.

    Args:
         Diccionario de datos agregados.

    Returns:
        Lista de strings con las claves.
    """
    return list(data.keys())


if __name__ == '__main__':
    sales_by_cat = {'Electronica': 300.0, 'Hogar': 50.0}
    print(extract_chart_labels(sales_by_cat))
