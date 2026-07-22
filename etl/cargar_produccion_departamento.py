import os
import pandas as pd
from conexion import obtener_conexion


# ==========================
# 1 - EXTRACCION
# ==========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

archivo = os.path.join(
    BASE_DIR,
    "..",
    "datasets",
    "raw",
    "mani-serie-1927-2024.csv"
)

df = pd.read_csv(
    archivo,
    encoding="latin-1"
)

print("\nDataset cargado:")
print(df.head())

print("\nColumnas:")
print(df.columns)

print("\nCantidad de registros:")
print(df.shape)

# ==========================
# 2 - TRANSFORMACION
# ==========================

conexion = obtener_conexion()

query = """
SELECT
    id,
    departamento_id_dataset
FROM departamento
"""

df_departamentos = pd.read_sql(query, conexion)

print("\nDepartamentos MySQL:")
print(df_departamentos.head())

print("\nCantidad departamentos:")
print(len(df_departamentos))

# -----------------------------------
# Control antes del merge
# -----------------------------------

cantidad_original = len(df)

print("\nRegistros originales:")
print(cantidad_original)

df = df.merge(
    df_departamentos,
    left_on="departamento_id",
    right_on="departamento_id_dataset",
    how="left"
)

print("\nRegistros luego del merge:")
print(len(df))

print("\nFilas agregadas por el merge:")
print(len(df) - cantidad_original)

print("\nDepartamentos sin relacion:")
print(df["id"].isna().sum())

duplicados = df_departamentos[
    df_departamentos.duplicated(
        subset=["departamento_id_dataset"],
        keep=False
    )
]

print(duplicados.sort_values("departamento_id_dataset"))

# ==========================
# 3 - PREPARAR CARGA
# ==========================

df_final = df[
    [
        "anio",
        "campania",
        "id",
        "superficie_sembrada_ha",
        "superficie_cosechada_ha",
        "produccion_tm",
        "rendimiento_kgxha"
    ]
].copy()

df_final.columns = [
    "anio",
    "campania",
    "departamento_id",
    "superficie_sembrada_ha",
    "superficie_cosechada_ha",
    "produccion_tn",
    "rendimiento_kg_ha"
]

print("\nDataFrame final:")
print(df_final.head())

print("\nCantidad registros a insertar:")
print(len(df_final))

# ==========================
# 3 - CARGA MYSQL
# ==========================

print("\nInsertando produccion departamental...")


df_final.to_sql(
    "produccion_departamento",
    conexion,
    if_exists="append",
    index=False
)


print("\nCarga produccion departamental finalizada correctamente")

