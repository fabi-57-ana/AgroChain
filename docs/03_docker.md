# AgroChain - Uso de Docker


## 1. Introducción

Docker es una plataforma que permite ejecutar aplicaciones dentro de contenedores.

Un contenedor es un entorno aislado que contiene todo lo necesario para ejecutar un servicio, incluyendo configuración, dependencias y herramientas necesarias.

A diferencia de una instalación tradicional, Docker permite crear entornos reproducibles, evitando problemas relacionados con diferencias entre equipos o configuraciones.


## 2. ¿Por qué se utilizó Docker en AgroChain?

Dentro del proyecto AgroChain, Docker fue utilizado principalmente para ejecutar la base de datos MySQL en un entorno controlado.

La utilización de un contenedor permitió:

- evitar instalar MySQL directamente en el sistema operativo;
- mantener una configuración independiente del equipo;
- facilitar la creación y eliminación del entorno;
- conservar los datos mediante persistencia.


La arquitectura del entorno quedó conformada por:
```text
Proyecto AgroChain
        |
        |
+----------------+
|                |
v                v
Python ETL Contenedor Docker
        |
        v
      MySQL
```

## 3. Componentes utilizados


### Docker Desktop

Se utilizó Docker Desktop como plataforma para administrar los contenedores desde Windows.


### Contenedor MySQL

Se creó un contenedor encargado de ejecutar el motor de base de datos MySQL.

Dentro del contenedor se almacenan las tablas utilizadas por el proyecto:

- provincia;
- departamento;
- producción anual;
- producción departamental.


## 4. Funcionamiento del entorno


El flujo de trabajo fue:


### 1. Inicio del contenedor

Se inicia el servicio MySQL mediante Docker.


Ejemplo:


docker start agrochain-mysql

2. Acceso a la base de datos

Los scripts Python se conectan al servidor MySQL que se encuentra ejecutándose dentro del contenedor.

La conexión permite:

crear tablas;
cargar datos mediante ETL;
realizar consultas SQL.
3. Ejecución de procesos ETL

Los scripts desarrollados en Python procesan los datasets y envían la información transformada hacia MySQL.

Flujo:
```text
Archivo CSV
     |
     v
Python + Pandas
     |
     v
MySQL dentro de Docker
```
5. Persistencia de datos

El uso de Docker permite mantener la información almacenada aunque el contenedor sea detenido.

La persistencia evita perder:

estructura de tablas;
registros cargados;
datos procesados.

Esto permite continuar el desarrollo sin necesidad de reconstruir la base desde cero.

6. Ventajas obtenidas

El uso de Docker aportó:

organización del entorno de desarrollo;
separación entre aplicación y base de datos;
facilidad para reproducir el proyecto;
menor dependencia de configuraciones locales.
7. Relación con la arquitectura general

Docker forma parte de la infraestructura de soporte del sistema.

El flujo completo queda:
```text
Dataset agrícola
        |
        v
Procesos ETL Python
        |
        v
MySQL ejecutándose en Docker
        |
        +----------------+
        |                |
        v                v
Consultas SQL      Blockchain
                         |
                         v
                 datos_cadena.json
```

8. Conclusión

Docker permitió implementar un entorno estable y reproducible para AgroChain, facilitando la integración entre los procesos ETL desarrollados en Python y la base de datos MySQL.

Aunque Docker no constituye el objetivo principal del proyecto, fue una herramienta fundamental para organizar y mantener la infraestructura utilizada durante el desarrollo.



