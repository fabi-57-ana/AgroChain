from cadena import Blockchain
import pandas as pd
import sys
import os
import json

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "etl"
    )
)

from conexion import obtener_conexion

print("=" * 50)
print("CARGA DE DATOS PRODUCTIVOS EN BLOCKCHAIN")
print("=" * 50)


# ==========================
# 1 - CONEXION MYSQL
# ==========================

conexion = obtener_conexion()


# ==========================
# 2 - CONSULTA PRODUCTIVA
# ==========================

query = """
SELECT
    p.nombre AS provincia,
    d.nombre AS departamento,
    pd.anio,
    pd.produccion_tn,
    pd.rendimiento_kg_ha

FROM produccion_departamento pd

JOIN departamento d
    ON pd.departamento_id = d.id

JOIN provincia p
    ON d.provincia_id = p.id

WHERE pd.anio = 2024

ORDER BY pd.produccion_tn DESC

LIMIT 5;
"""


df = pd.read_sql(
    query,
    conexion
)


print("\nDatos seleccionados:")
print(df)


# ==========================
# 3 - CREACION BLOCKCHAIN
# ==========================

cadena = Blockchain()


# ==========================
# 4 - CREACION DE BLOQUES
# ==========================

for _, fila in df.iterrows():

    datos = {
        "cultivo": "mani",
        "anio": int(fila["anio"]),
        "provincia": fila["provincia"],
        "departamento": fila["departamento"],
        "produccion_tn": float(fila["produccion_tn"]),
        "rendimiento_kg_ha": float(fila["rendimiento_kg_ha"])
    }


    cadena.agregar_bloque(
        datos
    )


# ==========================
# 5 - MOSTRAR CADENA
# ==========================

print("\nCADENA BLOCKCHAIN:")
cadena.mostrar_cadena()


# ==========================
# 6 - VALIDACION
# ==========================

print("\nVALIDACION DE CADENA:")

print(
    cadena.validar_cadena()
)

# ==========================
# 7 - PERSISTENCIA JSON
# ==========================

archivo_json = "blockchain/datos_cadena.json"


cadena_json = []


for bloque in cadena.cadena:

    cadena_json.append(
        {
            "indice": bloque.indice,
            "fecha": str(bloque.timestamp),
            "datos": bloque.datos,
            "hash_anterior": bloque.hash_anterior,
            "hash": bloque.hash
        }
    )


with open(
    archivo_json,
    "w",
    encoding="utf-8"
) as archivo:

    json.dump(
        cadena_json,
        archivo,
        indent=4,
        ensure_ascii=False
    )


print("\nCadena guardada en:")
print(archivo_json)