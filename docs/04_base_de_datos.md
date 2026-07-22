# AgroChain - Base de Datos


## 1. Introducción

La base de datos de AgroChain fue diseñada para almacenar y organizar la información histórica de producción de maní proveniente de datasets agrícolas.

Su función principal es servir como capa de almacenamiento estructurada entre los procesos ETL desarrollados en Python y los módulos de análisis y trazabilidad blockchain.


## 2. Motor utilizado

Se utilizó:

- MySQL 8
- Ejecutado mediante un contenedor Docker


La utilización de MySQL permitió:

- almacenar datos estructurados;
- realizar consultas SQL;
- relacionar información mediante claves primarias y relaciones entre tablas.


## 3. Modelo de datos


La base de datos está compuesta principalmente por:


### Tabla provincia

Almacena las provincias relacionadas con los datos productivos.


Campos principales:

- id
- provincia_id_dataset
- nombre



### Tabla departamento

Almacena los departamentos productivos asociados a cada provincia.


Campos principales:

- id
- departamento_id_dataset
- nombre
- provincia_id


Relación:

Provincia 1 -------- N Departamento




### Tabla produccion_anual

Contiene la evolución histórica nacional del cultivo de maní.


Información almacenada:

- año
- producción total
- rendimiento
- superficie sembrada
- superficie cosechada


Periodo:

1927 - 2024



### Tabla produccion_departamento

Contiene información productiva a nivel departamental.


Permite consultar:

- producción por provincia;
- producción por departamento;
- rendimiento;
- distribución geográfica del cultivo.


Periodo:

1927 - 2024



## 4. Flujo de carga de datos


El proceso utilizado fue:

Dataset CSV
    |
    v
Python + Pandas
    |
    v
Procesos ETL
    |
    v
Base MySQL
    |
    v
Consultas SQL



## 5. Validaciones realizadas


Durante la carga se verificó:

- cantidad de registros procesados;
- relación correcta entre departamentos y provincias;
- ausencia de registros sin correspondencia;
- rango temporal cargado.


Resultado final:

- Producción anual: 1927 - 2024
- Producción departamental: 5257 registros


## 6. Relación con Blockchain


La base de datos funciona como fuente de información para seleccionar registros productivos que luego son incorporados a la cadena blockchain.


Flujo:

   MySQL
    |
    v
Registro productivo seleccionado
    |
    v
Bloque Blockchain
    |
    v
Hash y trazabilidad



## 7. Conclusión

La base de datos MySQL permitió estructurar la información agrícola histórica y generar una fuente confiable para los procesos de análisis y trazabilidad desarrollados en AgroChain.

