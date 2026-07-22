# AgroChain - Arquitectura del Sistema


## 1. Introducción

La arquitectura de AgroChain está diseñada para integrar procesamiento de datos agrícolas, almacenamiento estructurado y trazabilidad mediante blockchain.

El sistema se divide en diferentes capas, donde cada componente cumple una función específica dentro del flujo de información.


## 2. Arquitectura general

El flujo completo del sistema es:

             Dataset INTA
                  |
                  v
          Procesos ETL Python
                  |
                  v
            Base MySQL
                  |
    +-------------+-------------+
    |                           |
    v                           v
        Consultas productivas Blockchain
    |          |
    |          v
    | datos_cadena.json
    |
    v
    Análisis de producción agrícola



## 3. Capa de datos


### Dataset origen

El proyecto utiliza información histórica del cultivo de maní en Argentina.

Los datos contienen información productiva desde:

1927 - 2024


Incluyendo:

- año;
- campaña;
- provincia;
- departamento;
- superficie sembrada;
- superficie cosechada;
- producción;
- rendimiento.


## 4. Capa ETL


El procesamiento de datos se realiza mediante scripts desarrollados en Python.

La función del proceso ETL es:

### Extracción

Lectura de archivos CSV originales.


### Transformación

Procesamiento de datos:

- limpieza de estructuras;
- eliminación de duplicados;
- relación entre entidades geográficas;
- adaptación de formatos.


### Carga

Inserción de información transformada dentro de MySQL.


Los procesos principales son:

etl/
│
├── cargar_provincias.py
├── cargar_departamentos.py
├── cargar_produccion_anual.py
├── cargar_produccion_departamento.py
└── conexion.py


## 5. Capa de base de datos


La información procesada se almacena en MySQL mediante un modelo relacional.


Principales entidades:


### Provincia

Almacena información geográfica provincial.


### Departamento

Relaciona los departamentos productivos con su provincia correspondiente.


### Producción anual

Contiene indicadores históricos generales del cultivo.


### Producción departamental

Almacena datos productivos con mayor nivel de detalle territorial.


El modelo permite realizar consultas sobre:

- evolución histórica;
- producción por provincia;
- producción por departamento;
- rendimiento agrícola.


## 6. Capa de consultas productivas


Sobre la base de datos se desarrollaron consultas SQL orientadas al análisis.

Ejemplos:

- evolución histórica de producción;
- producción por provincia en 2024;
- principales departamentos productores;
- análisis del período tecnológico reciente.


Estas consultas permiten obtener información útil antes de aplicar mecanismos de trazabilidad.


## 7. Capa Blockchain


La blockchain implementada funciona como una prueba de concepto orientada a trazabilidad.


Cada bloque contiene:

- índice;
- fecha;
- datos productivos;
- hash propio;
- hash del bloque anterior.


Estructura:

Bloque anterior
       |
       v
+----------------+
| Bloque actual  |
+----------------+
       |
       v
Hash encadenado



La cadena permite validar que los registros no fueron modificados después de ser almacenados.


## 8. Persistencia de trazabilidad


Luego de validar la cadena, la información se almacena en:

blockchain/datos_cadena.json



Este archivo conserva:

- bloques generados;
- datos productivos registrados;
- hashes;
- relación entre bloques.


## 9. Tecnologías utilizadas


| Componente           | Tecnología              |
|----------------------|-------------------------|
| Procesamiento ETL    | Python                  |
| Manipulación de datos| Pandas                  |
| Base de datos        | MySQL                   |
| Entorno de ejecución | Docker                  |
| Trazabilidad         | Blockchain experimental |
| Persistencia         | JSON                    |


## 10. Alcance de la arquitectura


La arquitectura implementada corresponde a una prueba de concepto académica.

Incluye:

- integración de datos agrícolas;
- procesamiento ETL;
- almacenamiento relacional;
- análisis productivo;
- trazabilidad blockchain.


No incluye:

- blockchain distribuida entre nodos;
- minería;
- contratos inteligentes;
- conexión con sensores en tiempo real.


## 11. Resultado

La arquitectura permite demostrar cómo un flujo de datos agropecuarios puede evolucionar desde un dataset histórico hasta un registro productivo con mecanismos básicos de integridad y trazabilidad digital.

