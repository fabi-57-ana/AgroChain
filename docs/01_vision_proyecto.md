# AgroChain - Visión del Proyecto


## 1. Introducción

AgroChain es un proyecto orientado a la aplicación de tecnologías de datos y blockchain en el sector agropecuario.

El objetivo es construir un sistema que permita analizar información histórica de producción agrícola y demostrar cómo un registro productivo puede adquirir características de trazabilidad mediante una cadena de bloques.

El proyecto utiliza como caso de estudio el cultivo de maní en Argentina, utilizando datos históricos productivos a nivel nacional, provincial y departamental.


## 2. Problemática

La actividad agropecuaria genera grandes volúmenes de información relacionados con producción, rendimiento y distribución territorial.

Sin embargo, disponer de datos históricos no garantiza por sí mismo la trazabilidad de la información utilizada.

Surge entonces la necesidad de integrar herramientas que permitan:

- almacenar información productiva de manera estructurada;
- facilitar el análisis de datos históricos;
- conservar registros verificables;
- mejorar la transparencia sobre la información generada.


## 3. Objetivo del proyecto

Desarrollar una arquitectura tecnológica que integre procesamiento de datos y blockchain para analizar y registrar información productiva del cultivo de maní.


## 4. Objetivos específicos

- Incorporar un dataset histórico de producción agrícola.
- Diseñar procesos ETL para transformar y cargar información en una base de datos.
- Organizar la información productiva mediante un modelo relacional.
- Realizar consultas orientadas al análisis productivo.
- Implementar una blockchain experimental para registrar datos seleccionados.
- Validar la integridad de los registros mediante hashes encadenados.
- Persistir la información registrada para conservar evidencia de trazabilidad.


## 5. Caso de estudio

El proyecto utiliza como fuente de información datos históricos del cultivo de maní en Argentina.

El dataset contiene información como:

- año de producción;
- campaña agrícola;
- provincia;
- departamento;
- superficie sembrada;
- superficie cosechada;
- producción obtenida;
- rendimiento.


El período analizado comprende desde el año 1927 hasta 2024.


## 6. Enfoque tecnológico

La solución integra diferentes tecnologías:

### Ciencia de datos

Utilizada para explorar, analizar y comprender el comportamiento histórico de la producción agrícola.


### ETL

Desarrollado mediante Python para:

- extraer datos desde archivos originales;
- transformar estructuras;
- relacionar entidades geográficas;
- cargar información en la base de datos.


### Base de datos

Se utiliza MySQL para almacenar la información productiva de manera organizada y permitir consultas analíticas.


### Blockchain

Se implementa una blockchain experimental orientada a la trazabilidad.

Los registros productivos seleccionados son almacenados en bloques con:

- índice;
- fecha;
- datos productivos;
- hash propio;
- referencia al hash del bloque anterior.

Esto permite verificar si la información registrada fue modificada.


## 7. Arquitectura general

El flujo general del proyecto es:

```text
Dataset productivo
        │
        ▼
Procesos ETL con Python
        │
        ▼
Base de datos MySQL
        │
   ┌────┴────────────┐
   │                 │
   ▼                 ▼
Consultas        Blockchain
productivas          │
                     ▼
             Registro trazable
            datos_cadena.json
```


## 8. Alcance del proyecto

El proyecto se enfoca en demostrar una integración tecnológica aplicada al agro.

Incluye:

- procesamiento de datos históricos;
- almacenamiento estructurado;
- análisis productivo;
- prueba de concepto blockchain.


No contempla:

- una red blockchain distribuida real;
- contratos inteligentes;
- criptomonedas;
- integración con productores en tiempo real.


## 9. Resultado esperado

Obtener una plataforma experimental donde los datos históricos de producción agrícola puedan ser analizados y donde determinados registros productivos puedan ser almacenados con mecanismos básicos de trazabilidad.

La propuesta busca demostrar cómo tecnologías emergentes pueden aportar valor al sector agropecuario mediante la combinación de datos y confianza digital.

