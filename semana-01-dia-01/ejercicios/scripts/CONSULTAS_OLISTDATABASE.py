import warnings  # [NUEVO: Para silenciar advertencias]

import pandas as pd
import pyodbc

# 1. Silenciamos el mensaje amarillo para que no estorbe
warnings.filterwarnings('ignore')

conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=localhost\\MAESTRIA;"
    "Database=Proyecto_Olist_Calidad;"
    "Trusted_Connection=yes;"
    "Encrypt=no;"
)

query = """
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE = 'BASE TABLE'
        ORDER BY CASE \
                     WHEN TABLE_NAME LIKE 'Dim_%' THEN 1 \
                     WHEN TABLE_NAME LIKE 'Fact_%' THEN 2 \
                     ELSE 3 \
                     END, \
                 TABLE_NAME \
        """

try:
    with pyodbc.connect(conn_str) as conn:
        # 2. Leemos los datos
        df = pd.read_sql(query, conn)

        # 3. FORZAMOS LA IMPRESIÓN (Si esto no sale, el problema es la conexión)
        print("\n" + "=" * 60)
        print("📊 INGENIERÍA DE DATOS: MAPA DE TABLAS OLIST")
        print("=" * 60)

        if df.empty:
            print("⚠️ La consulta no devolvió datos. Revisa el nombre de la DB.")
        else:
            print(df.to_string(index=False))  # index=False lo hace ver más limpio

        print("=" * 60)
        print("✅ PROCESO FINALIZADO CON ÉXITO")

except Exception as e:
    print(f"❌ ERROR CRÍTICO: {e}")
