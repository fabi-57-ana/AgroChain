import os

import pandas as pd

from conexion import obtener_conexion


print("=" * 40)
print("CARGA DEPARTAMENTOS")
print("=" * 40)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


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

df = pd.read_csv(
    archivo,
    encoding="latin-1"
)


print("\nDataset cargado:")
print(df.head())


# ==========================
# 2 - TRANSFORMACIÓN
# ==========================


# Extraemos departamentos únicos

departamentos = (
    df[
        [
            "departamento_id",
            "departamento",
            "provincia_id"
        ]
    ]
    .drop_duplicates()
    .drop_duplicates(
        subset=["departamento_id"],
        keep="first"
    )
)


print("\nDepartamentos encontrados:")
print(departamentos.head())


print("\nCantidad:")
print(len(departamentos))


# ==========================
# Buscar IDs internos de provincia
# ==========================


conexion = obtener_conexion()


provincias_mysql = pd.read_sql(
    """
    SELECT 
        id,
        provincia_id_dataset
    FROM provincia
    """,
    conexion
)


print("\nProvincias MySQL:")
print(provincias_mysql.head())


# Relacionamos dataset con tabla provincia

departamentos = departamentos.merge(
    provincias_mysql,
    left_on="provincia_id",
    right_on="provincia_id_dataset",
    how="left"
)


# Eliminamos columnas que no necesitamos

departamentos = departamentos[
    [
        "departamento_id",
        "departamento",
        "id"
    ]
]


departamentos.columns = [
    "departamento_id_dataset",
    "nombre",
    "provincia_id"
]


print("\nResultado final:")
print(departamentos.head())


# ==========================
# 3 - CARGA MYSQL
# ==========================


print("\nInsertando departamentos...")


departamentos.to_sql(
    "departamento",
    conexion,
    if_exists="append",
    index=False
)


print("\nCarga departamentos finalizada correctamente")

