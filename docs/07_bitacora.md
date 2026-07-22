# Bitácora del Proyecto AgroChain

La presente bitácora resume las principales actividades realizadas durante el desarrollo del proyecto AgroChain. Se documentan las etapas implementadas, las decisiones técnicas adoptadas y los resultados obtenidos durante la construcción del sistema.


# Configuración del entorno de desarrollo

## Objetivo

Preparar el entorno de trabajo necesario para el desarrollo del proyecto.

## Actividades realizadas

* Configuración del entorno Python mediante un entorno virtual (`.venv`).
* Configuración de Docker Compose.
* Implementación del servicio MySQL 8.0 en un contenedor Docker.
* Creación de la base de datos `agrochain`.
* Organización de la estructura inicial del proyecto.

## Resultado

El entorno quedó preparado para comenzar el desarrollo del modelo de datos y de los procesos ETL.

## ETL de Producción Anual
Objetivo

Implementar el primer proceso ETL del proyecto.

Archivo desarrollado
etl/cargar_produccion.py
Actividades realizadas
Lectura del dataset anual.
Transformación de columnas.
Inserción mediante SQLAlchemy.
Validación de registros cargados.
Resultado
98 registros cargados correctamente.
Período almacenado: 1927–2024.

## ETL de Provincias
Objetivo

Construir la tabla maestra de provincias.

Archivo desarrollado
etl/cargar_provincias.py
Actividades realizadas
Extracción de provincias únicas.
Eliminación de duplicados.
Inserción en MySQL.
Incidencia

Durante la carga se detectó un problema de codificación de caracteres.

Solución

Se utilizó el encoding latin-1 para interpretar correctamente los nombres con caracteres especiales.

Resultado
18 provincias cargadas correctamente.

## ETL de Departamentos
Objetivo

Crear la tabla de departamentos vinculada con las provincias.

Archivo desarrollado
etl/cargar_departamentos.py
Actividades realizadas
Extracción de departamentos únicos.
Asociación con provincias.
Conversión del identificador del dataset al identificador interno de MySQL.
Resultado
283 departamentos cargados correctamente.

## ETL de Producción Departamental
Objetivo

Completar la carga histórica de producción de maní a nivel departamental.

Archivo desarrollado
etl/cargar_produccion_departamento.py
Actividades realizadas
Lectura del dataset departamental.
Relación con la tabla departamento.
Validación del proceso de merge.
Inserción de los registros históricos.
Validaciones
Registros originales: 5257
Registros luego del merge: 5257
Departamentos sin relación: 0
Resultado
5257 registros cargados correctamente.
Período almacenado: 1927–2024.

## Consultas Analíticas
Objetivo

Realizar consultas SQL para validar la información cargada y obtener indicadores productivos.

Archivo creado
sql/queries/01_consultas_productivas.sql
Consultas implementadas
Evolución histórica de la producción.
Producción por provincia (2024).
Ranking de departamentos productores.
Evolución productiva desde el año 2000.
Consulta preparada para Blockchain.
Resultado

Las consultas verificaron la correcta carga de la información y permitieron obtener indicadores productivos relevantes.

## Implementación Blockchain
Objetivo

Incorporar un mecanismo de trazabilidad utilizando una blockchain desarrollada en Python.

Archivos desarrollados
bloque.py
cadena.py
prueba_bloque.py
prueba_cadena.py
cargar_bloques_productivos.py
Actividades realizadas
Implementación de la clase Bloque.
Implementación de la cadena de bloques.
Creación del bloque génesis.
Incorporación de registros productivos reales.
Implementación de validación por hash.
Prueba de alteración de datos para verificar integridad.
Exportación de la cadena al archivo datos_cadena.json.
Resultado

Se obtuvo una blockchain funcional que demuestra la trazabilidad e integridad de registros productivos del cultivo de maní.

Estado actual del proyecto

Completado

Infraestructura Docker.
Base de datos MySQL.
Modelo relacional.
Procesos ETL.
Consultas analíticas.
Blockchain funcional.
Persistencia de la cadena en formato JSON.

## Próximo paso

Preparar la documentación final y la presentación del proyecto, integrando el flujo completo:

Big Data → ETL → MySQL → Blockchain → Trazabilidad Agropecuaria

