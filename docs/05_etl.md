# ETL - Proceso de carga de datos AgroChain

## 1. Introducción

El proceso ETL (Extract, Transform, Load) es el encargado de integrar los datos agrícolas provenientes de archivos CSV con la base de datos MySQL del proyecto AgroChain.

Su función consiste en extraer la información de los datasets originales, transformarla para adaptarla al modelo relacional diseñado y cargarla en la base de datos, preservando la integridad y consistencia de la información.

Los archivos originales nunca son modificados, ya que constituyen la fuente oficial de datos del proyecto.


# 2. Arquitectura del proceso ETL

El flujo general implementado es el siguiente:


Datasets CSV
      │
      ▼
 Extracción
      │
      ▼
 Transformación
      │
      ▼
 Validación
      │
      ▼
 Carga en MySQL
      │
      ▼
 Base de datos AgroChain



# 3. Datasets utilizados

Los archivos utilizados durante el desarrollo se encuentran en:

datasets/raw/


## Dataset anual

Archivo:

mani-serie-1927-2024-anual.csv


Características:

* 98 registros.
* Información histórica nacional.
* Período 1927–2024.

Tabla destino:

produccion_anual


## Dataset departamental

Archivo:

mani-serie-1927-2024.csv

Características:

* 5257 registros.
* Información histórica por provincia y departamento.
* Incluye campañas agrícolas.

Tablas destino:

provincia
departamento
produccion_departamento


# 4. Herramientas utilizadas

Durante el desarrollo del ETL se utilizaron las siguientes tecnologías:

## Python

Bibliotecas principales:

* pandas
* SQLAlchemy
* PyMySQL
* python-dotenv

## Base de datos

* MySQL 8
* Contenedor Docker

La conexión entre Python y MySQL se centralizó mediante el archivo:

etl/conexion.py


# 5. Procesos ETL implementados

Cada proceso fue desarrollado con una única responsabilidad, facilitando su mantenimiento y reutilización.


## 5.1 cargar_provincias.py

Objetivo:

Extraer las provincias presentes en el dataset y cargarlas en la tabla `provincia`.

Proceso realizado:

* lectura del dataset;
* selección de provincias únicas;
* eliminación de duplicados;
* inserción en MySQL.

Resultado:

* 18 provincias cargadas correctamente.

## 5.2 cargar_departamentos.py

Objetivo:

Extraer los departamentos únicos y relacionarlos con su provincia correspondiente.

Proceso realizado:

* lectura del dataset;
* extracción de departamentos;
* asociación con la tabla `provincia`;
* conversión del identificador del dataset al identificador interno de MySQL;
* inserción en la tabla `departamento`.

Resultado:

* 258 departamentos cargados correctamente.


## 5.3 cargar_produccion_anual.py

Objetivo:

Cargar la producción anual histórica del cultivo de maní.

Fuente:

mani-serie-1927-2024-anual.csv


Transformaciones realizadas:

* normalización de nombres de columnas;
* adaptación al modelo relacional;
* inserción mediante SQLAlchemy.

Tabla destino:

produccion_anual

Resultado:

* 98 registros cargados.
* Período almacenado: 1927–2024.


## 5.4 cargar_produccion_departamento.py

Objetivo:

Cargar los registros históricos de producción de maní por departamento.

Fuente:

mani-serie-1927-2024.csv

Proceso realizado:

1. Lectura del dataset.
2. Selección de las columnas necesarias.
3. Obtención del identificador interno del departamento.
4. Asociación mediante `departamento_id_dataset`.
5. Preparación del DataFrame final.
6. Inserción en MySQL.

Tabla destino:

produccion_departamento

Validaciones realizadas:

* registros originales: 5257;
* registros luego del merge: 5257;
* filas agregadas por duplicación: 0;
* departamentos sin relación: 0.

Resultado:

* 5257 registros cargados correctamente.


# 6. Validaciones realizadas

Durante la implementación del proceso ETL se verificó:

* correcta lectura de ambos datasets;
* eliminación de registros duplicados;
* correspondencia entre provincias y departamentos;
* integridad de las relaciones entre tablas;
* inserción completa de los registros;
* rango temporal almacenado.

Resultados obtenidos:

| Tabla                   | Registros |
| ----------------------- | --------: |
| provincia               |        18 |
| departamento            |       258 |
| produccion_anual        |        98 |
| produccion_departamento |      5257 |

Rango temporal validado:

* primer año: 1927;
* último año: 2024.


# 7. Buenas prácticas aplicadas

Durante el desarrollo se siguieron las siguientes prácticas:

* mantener inalterados los datasets originales;
* separar extracción, transformación y carga;
* utilizar variables de entorno para las credenciales;
* implementar un script independiente para cada proceso ETL;
* validar los datos antes de cargarlos en la base de datos;
* documentar cada etapa del proceso.


# 8. Resultado final

El proceso ETL permitió construir la base de datos relacional de AgroChain a partir de los datasets históricos de producción de maní.

Las tablas generadas constituyen la fuente de información utilizada posteriormente para:

* consultas analíticas mediante SQL;
* obtención de indicadores productivos;
* selección de registros para la cadena blockchain;
* demostración de la trazabilidad de información agrícola.

El flujo implementado quedó completamente operativo, permitiendo repetir el proceso de carga de manera controlada y reproducible cuando sea necesario.
