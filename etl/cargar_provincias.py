import os

import pandas as pd

from conexion import obtener_conexion


print("=" * 40)
print("CARGA PROVINCIAS")
print("=" * 40)


# Ubicación del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Dataset completo
archivo = os.path.join(
    BASE_DIR,
    "..",
    "datasets",
    "raw",
    "mani-serie-1927-2024.csv"
)


# ==========================
# 1 - EXTRACCIÓN
# ==========================

# Le agregamos el encoding "latin-1"
df = pd.read_csv(archivo, encoding="latin-1")


print("\nDataset cargado:")
print(df.head())

# ==========================
# 2 - TRANSFORMACIÓN
# ==========================

provincias = (
    df[["provincia_id", "provincia"]]
    .drop_duplicates()
    .sort_values("provincia")
)


print("\nProvincias encontradas:")
print(provincias)


print("\nCantidad:")
print(len(provincias))


# Renombrar columnas para MySQL

provincias.columns = [
    "provincia_id_dataset",
    "nombre"
]


# ==========================
# 3 - CARGA MYSQL
# ==========================

conexion = obtener_conexion()


print("\nInsertando provincias...")


provincias.to_sql(
    "provincia",
    conexion,
    if_exists="append",
    index=False
)


print("\nCarga provincias finalizada correctamente")