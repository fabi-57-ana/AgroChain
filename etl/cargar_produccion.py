import os

import pandas as pd

from conexion import obtener_conexion


print("=" * 40)
print("CARGA PRODUCCION ANUAL")
print("=" * 40)


# Directorio actual del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Ruta del dataset
archivo = os.path.join(
    BASE_DIR,
    "..",
    "datasets",
    "raw",
    "mani-serie-1927-2024-anual.csv"
)


# ==========================
# 1 - EXTRACCIÓN
# ==========================

df = pd.read_csv(archivo)


print("\nDataset original:")
print(df.head())


# ==========================
# 2 - TRANSFORMACIÓN
# ==========================

# Normalizamos nombres de columnas

df.columns = [
    "anio",
    "superficie_sembrada_ha",
    "superficie_cosechada_ha",
    "produccion_tn",
    "rendimiento_kg_ha"
]


print("\nColumnas transformadas:")
print(df.columns)


print("\nCantidad registros:")
print(df.shape)


# ==========================
# 3 - CARGA MYSQL
# ==========================

conexion = obtener_conexion()


print("\nInsertando datos en MySQL...")


df.to_sql(
    "produccion_anual",
    conexion,
    if_exists="append",
    index=False
)


print("\nCarga finalizada correctamente")