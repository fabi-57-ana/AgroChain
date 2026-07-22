# AgroChain

## Sistema de gestión y trazabilidad de datos productivos agrícolas utilizando ETL, MySQL y Blockchain

## Descripción del proyecto

AgroChain es un proyecto desarrollado como parte de la Tecnicatura en Nuevas Tecnologías Aplicadas al Agro.

El proyecto integra diferentes tecnologías para construir un flujo completo de procesamiento de datos agrícolas, comenzando con la extracción de información desde archivos CSV, continuando con su transformación e incorporación a una base de datos relacional y finalizando con la implementación de una blockchain que permite demostrar la trazabilidad e integridad de los registros productivos.

Como caso de estudio se utilizó información histórica del cultivo de maní en Argentina, empleando datasets públicos que contienen registros nacionales y departamentales correspondientes al período 1927–2024.

El desarrollo integra conceptos de ingeniería de datos, bases de datos, automatización de procesos ETL, contenedores Docker y blockchain, mostrando cómo estas tecnologías pueden combinarse para construir soluciones aplicadas al sector agropecuario.

# Objetivos

## Objetivo general

Desarrollar un sistema capaz de procesar información histórica del cultivo de maní mediante un flujo ETL, almacenarla en una base de datos relacional y demostrar la trazabilidad de los registros utilizando una blockchain desarrollada en Python.

## Objetivos específicos

* Diseñar un modelo relacional para almacenar información agrícola.
* Automatizar la carga de datos mediante procesos ETL desarrollados en Python.
* Gestionar la base de datos utilizando MySQL ejecutándose dentro de un contenedor Docker.
* Realizar consultas SQL para obtener indicadores productivos.
* Implementar una blockchain simplificada para demostrar la integridad y trazabilidad de los registros agrícolas.
* Documentar todas las etapas del desarrollo para facilitar la instalación, reproducción y mantenimiento del proyecto.


# Alcance del proyecto

AgroChain fue desarrollado con fines educativos como un proyecto integrador para demostrar la integración de distintas tecnologías aplicadas al procesamiento y análisis de datos agropecuarios.

El proyecto no pretende reemplazar sistemas productivos comerciales, sino servir como una prueba de concepto que muestre un flujo completo de trabajo, desde la obtención de los datos hasta la validación de su integridad mediante blockchain.

# Flujo general del sistema

Datasets CSV
      │
      ▼
Procesos ETL (Python)
      │
      ▼
MySQL (Docker)
      │
      ├──────────────► Consultas SQL
      │
      ▼
Blockchain
      │
      ▼
Trazabilidad de registros productivos

# Características principales

* Procesamiento automatizado de datos históricos del cultivo de maní.
* Procesos ETL desarrollados en Python utilizando pandas y SQLAlchemy.
* Base de datos MySQL ejecutándose mediante Docker.
* Modelo relacional normalizado con tablas para provincias, departamentos y producción agrícola.
* Consultas SQL para análisis productivo y validación de la información.
* Blockchain desarrollada en Python para demostrar la integridad de los registros.
* Persistencia de la cadena de bloques en formato JSON.
* Documentación técnica completa del proyecto.



# 🛠 Tecnologías utilizadas

AgroChain fue desarrollado utilizando herramientas ampliamente empleadas en proyectos de ingeniería de datos, desarrollo de software y análisis de información. Cada tecnología cumple una función específica dentro de la arquitectura del sistema.

| Tecnología              | Función dentro del proyecto                                                                                                           |
| ----------------------- | -------------------------------------------------------------------------------------- |
| **Python 3**            | Lenguaje principal utilizado para desarrollar los procesos ETL y la implementación de la blockchain.               |
| **Docker**              | Permite ejecutar MySQL dentro de un contenedor aislado, garantizando un entorno reproducible e independiente del sistema operativo.                                                                |
| **Docker Compose**      | Automatiza la creación y administración del contenedor de MySQL mediante un único archivo de configuración.         |
| **MySQL 8.0**           | Motor de base de datos relacional utilizado para almacenar toda la información agrícola procesada.                |
| **SQLAlchemy**          | ORM utilizado para establecer la conexión entre Python y MySQL y realizar la carga automática de datos.      |
| **Pandas**              | Biblioteca utilizada para leer, transformar y preparar los datasets CSV antes de cargarlos en la base de datos.                                                                                     |
| **PyMySQL**             | Controlador de conexión entre SQLAlchemy y MySQL.                                      |
| **python-dotenv**       | Permite almacenar las credenciales de conexión en un archivo `.env`, evitando escribir datos sensibles dentro del código.                                                                                 |
| **Git**                 | Control de versiones del proyecto.                                                     |
| **GitHub**              | Repositorio remoto utilizado para almacenar y compartir el proyecto.                   |
| **Blockchain (Python)** | Implementación propia de una cadena de bloques simplificada para demostrar la trazabilidad e integridad de registros productivos.                                                                |


# Arquitectura general del sistema

El proyecto se encuentra organizado en módulos independientes que colaboran entre sí para procesar los datos desde su origen hasta su almacenamiento y validación.

                    DATASETS
            (Archivos CSV originales)
                       │
                       ▼
              ETL desarrollado en Python
         (Extracción - Transformación - Carga)
                       │
                       ▼
              Base de datos MySQL 8.0
               (Contenedor Docker)
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
 Consultas SQL               Blockchain
 (Análisis de datos)      (Trazabilidad)
          │                         │
          └────────────┬────────────┘
                       ▼
              Información validada
             y lista para análisis


# Componentes del proyecto

## 1. Datasets

El proyecto utiliza dos conjuntos de datos históricos del cultivo de maní:

* Serie histórica anual (1927–2024).
* Serie histórica por provincia y departamento (1927–2024).

Estos archivos se almacenan dentro de:

datasets/raw/

## 2. Procesos ETL

Los procesos ETL son responsables de preparar toda la información antes de almacenarla en la base de datos.

Las tareas realizadas incluyen:

* Lectura de archivos CSV.
* Limpieza de datos.
* Transformación de columnas.
* Normalización de identificadores.
* Inserción automática en MySQL.

Todos los procesos se encuentran en:

etl/

## 3. Base de datos

La base de datos almacena la información transformada mediante un modelo relacional.

Tablas principales:

* `provincia`
* `departamento`
* `produccion_anual`
* `produccion_departamento`

Toda la estructura fue creada mediante scripts SQL versionados.


## 4. Consultas SQL

Una vez cargados los datos, se ejecutan consultas para obtener información productiva, tales como:

* Evolución histórica de la producción.
* Producción por provincia.
* Ranking de departamentos.
* Indicadores tecnológicos.
* Datos preparados para blockchain.


## 5. Blockchain

La blockchain implementada en Python representa una prueba de concepto de trazabilidad agrícola.

Cada bloque almacena información productiva junto con:

* índice,
* fecha de creación,
* datos,
* hash del bloque,
* hash del bloque anterior.

La cadena puede validarse automáticamente para comprobar que ningún bloque fue modificado.

Además, la blockchain puede persistirse en un archivo JSON para conservar la trazabilidad generada.


# Flujo completo del proyecto

CSV
 │
 ▼
Python (ETL)
 │
 ▼
MySQL (Docker)
 │
 ├────────► Consultas SQL
 │
 └────────► Blockchain
                 │
                 ▼
       Validación e integridad
       de registros agrícolas

# Filosofía del proyecto

AgroChain fue desarrollado siguiendo una arquitectura modular, donde cada componente tiene una única responsabilidad.

Esta organización facilita:

* el mantenimiento del código,
* la incorporación de nuevos datasets,
* la reutilización de los procesos ETL,
* la ampliación del modelo de datos,
* la integración futura con aplicaciones web, dashboards o APIs,
* la incorporación de nuevos mecanismos de trazabilidad basados en blockchain.


# Instalación completa

Esta sección describe el procedimiento completo para ejecutar AgroChain desde cero en un equipo nuevo.


# Requisitos previos

Antes de comenzar es necesario tener instalado:

* Git
* Python 3.11 o superior
* Docker Desktop
* Visual Studio Code (recomendado)

Verificar las instalaciones desde una terminal:

python --version
git --version
docker --version
docker compose version

Si todos los comandos muestran una versión instalada, el entorno está listo.


# 1. Clonar el repositorio

Abrir PowerShell y ejecutar:

git clone https://github.com/fabi-57-ana/AgroChain.git

Ingresar al proyecto:

cd AgroChain

# 2. Crear el entorno virtual

Crear un entorno virtual de Python:

python -m venv .venv

Activarlo:

Windows (PowerShell)

.venv\Scripts\Activate.ps1

Si la activación fue correcta aparecerá:

(.venv)

al comienzo de la línea de comandos.


# 3. Instalar las dependencias

Instalar todas las bibliotecas necesarias:

pip install -r requirements.txt

Verificar que la instalación finalizó correctamente:

pip list

Entre los paquetes instalados deberán encontrarse, al menos:

* pandas
* SQLAlchemy
* PyMySQL
* python-dotenv


# 4. Configurar las variables de entorno

En la carpeta principal del proyecto crear un archivo llamado:

.env

Contenido:

MYSQL_HOST=localhost
MYSQL_PORT=3307
MYSQL_DATABASE=agrochain
MYSQL_ROOT_PASSWORD=tu_password


Reemplazar **tu_password** por la contraseña utilizada para MySQL.

**Importante:** el archivo `.env` no debe subirse al repositorio ya que contiene credenciales de acceso.

# 5. Iniciar Docker

Abrir Docker Desktop y esperar hasta que indique que el motor de Docker está en ejecución.

Desde la carpeta del proyecto ejecutar:

docker compose up -d

Verificar que el contenedor esté funcionando:

docker ps

Debe aparecer un contenedor similar a:

agrochain-mysql

# 6. Acceder a MySQL

Ingresar al contenedor:

docker exec -it agrochain-mysql mysql -u root -p

Ingresar la contraseña configurada en el archivo `.env`.


# 7. Verificar la base de datos

Dentro de MySQL ejecutar:

SHOW DATABASES;

Seleccionar la base de datos:

USE agrochain;

Verificar las tablas:

SHOW TABLES;

Deberán existir las siguientes tablas:

* provincia
* departamento
* produccion_anual
* produccion_departamento

Salir de MySQL:

exit;

# 8. Ejecutar los procesos ETL

Todos los comandos deben ejecutarse desde la carpeta principal del proyecto.

## Producción anual

python etl/cargar_produccion.py

## Provincias

python etl/cargar_provincias.py

## Departamentos

python etl/cargar_departamentos.py

## Producción departamental

python etl/cargar_produccion_departamento.py

Cada script mostrará información del proceso y un mensaje indicando que la carga finalizó correctamente.

# 9. Ejecutar consultas SQL

Ingresar nuevamente a MySQL:

docker exec -it agrochain-mysql mysql -u root -p

Seleccionar la base:

USE agrochain;

Ejecutar las consultas incluidas en:

sql/queries/01_consultas_productivas.sql

También pueden copiarse y ejecutarse manualmente desde la consola de MySQL.

# 10. Ejecutar Blockchain

Probar un bloque individual:

python blockchain/prueba_bloque.py

Probar la cadena completa:

python blockchain/prueba_cadena.py

Cargar registros productivos reales desde la base de datos:

python blockchain/cargar_bloques_productivos.py

El script:

* obtiene registros desde MySQL,
* crea la blockchain,
* valida la integridad de la cadena,
* genera el archivo:

blockchain/datos_cadena.json

# 11. Estructura esperada del proyecto

Al finalizar la instalación la estructura principal será similar a:

AgroChain/
│
├── blockchain/
├── datasets/
├── docs/
├── etl/
├── sql/
├── .env
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore

# 12. Detener el proyecto

Para apagar los contenedores sin perder la información almacenada:

docker compose down

Los datos permanecerán guardados en el volumen de Docker.


# 13. Eliminar completamente el entorno

**Atención:** este procedimiento elimina la base de datos almacenada en Docker.

Detener los contenedores:

docker compose down

Eliminar el volumen:

docker volume rm agrochain_mysql_data

La próxima vez que se ejecute:

docker compose up -d

se creará una base de datos completamente vacía.


# 14. Solución de problemas

## El contenedor no aparece

Verificar:

docker ps

Si no está en ejecución:

docker compose up -d

## Error de conexión desde Python

Verificar:

* Docker Desktop iniciado.
* Contenedor `agrochain-mysql` en ejecución.
* Archivo `.env` correctamente configurado.
* Puerto `3307` disponible.

## Error con caracteres especiales (tildes y ñ)

Los datasets históricos utilizan codificación `latin-1`.

Todos los scripts ETL leen los archivos utilizando:

encoding="latin-1"

para preservar correctamente nombres de provincias y departamentos.

# Instalación finalizada

Si todos los pasos anteriores se ejecutaron correctamente, el proyecto AgroChain estará completamente operativo, con la base de datos cargada, las consultas disponibles y el módulo de blockchain listo para demostrar la trazabilidad de registros productivos.


# 🔄 Procesos ETL

El proyecto AgroChain implementa un proceso **ETL (Extract, Transform, Load)** para transformar los datos originales del cultivo de maní en información estructurada dentro de una base de datos relacional.

El flujo general del proceso es el siguiente:

Datasets CSV
      │
      ▼
 Extracción (Extract)
      │
      ▼
 Transformación (Transform)
      │
      ▼
 Carga en MySQL (Load)

Los procesos ETL fueron desarrollados en Python utilizando **Pandas** y **SQLAlchemy**, y se ejecutan de forma independiente según el tipo de información que se desea cargar.

Actualmente el proyecto cuenta con los siguientes procesos:

Script                                | Función                          -------------------------------------------------------------------------------------------------------------------|
| `cargar_produccion.py`              | Carga la serie histórica anual del cultivo de maní.                                 |                                                                            |
| `cargar_provincias.py`              | Obtiene las provincias únicas del dataset y las almacena en MySQL.                                |                                                                            |
| `cargar_departamentos.py`           | Carga los departamentos y establece su relación con cada provincia.                            |                                                                            |
| `cargar_produccion_departamento.py` | Inserta la producción histórica departamental relacionando cada registro con el departamento correspondiente.      |                                                                            |

Durante el proceso también se realizan transformaciones como:

* Normalización de nombres de columnas.
* Conversión de tipos de datos.
* Eliminación de registros duplicados.
* Relación entre identificadores del dataset e identificadores internos de MySQL.
* Validación de la cantidad de registros insertados.

Toda la documentación técnica del ETL se encuentra disponible en:

docs/05_etl.md

# Base de datos

AgroChain utiliza **MySQL 8.0** como sistema gestor de bases de datos, ejecutándose dentro de un contenedor Docker.

La base de datos almacena la información agrícola en un modelo relacional compuesto por cuatro tablas principales:

provincia
      │
      │
departamento
      │
      │
produccion_departamento

produccion_anual

Descripción de las tablas:

| Tabla                     | Descripción                                                 |
| ------------------------- | ----------------------------------------------------------- |
| `provincia`               | Provincias presentes en el dataset.                         |
| `departamento`            | Departamentos asociados a cada provincia.                   |
| `produccion_anual`        | Serie histórica nacional de producción de maní (1927–2024). |
| `produccion_departamento` | Producción histórica por departamento.                      |

El modelo fue diseñado para evitar redundancia de datos y facilitar consultas analíticas y procesos de trazabilidad.

La creación completa del esquema se encuentra en:

sql/schemas/01_schema.sql

Las consultas de análisis implementadas están disponibles en:

sql/queries/01_consultas_productivas.sql

# Blockchain

Como demostración de trazabilidad, AgroChain incorpora una implementación simplificada de blockchain desarrollada íntegramente en Python.

Cada bloque contiene:

* índice,
* fecha de creación,
* datos productivos,
* hash del bloque,
* hash del bloque anterior.

La estructura garantiza que cualquier modificación realizada sobre un bloque altere su hash y rompa la cadena, permitiendo detectar cambios en la información almacenada.

Los componentes implementados son:

Archivo                         |Función                                                                              
|------------------------------ |-----------------------------------------------------------------------------|
|`bloque.py`                    | Define la estructura y el cálculo del hash de cada bloque.                         
|`cadena.py`                    | Implementa la blockchain y la validación de integridad.                          
|`prueba_bloque.py`             | Prueba la creación de un bloque individual.                             
|`prueba_cadena.py`             | Prueba la creación y validación de una cadena de bloques.                         
|`cargar_bloques_productivos.py`| Construye una blockchain utilizando registros reales almacenados en MySQL y genera un archivo JSON con la trazabilidad.

Durante las pruebas se verificó que:

* la cadena se construye correctamente,
* los bloques mantienen la referencia al bloque anterior,
* cualquier modificación rompe la integridad de la cadena,
* la validación detecta automáticamente registros alterados.

El resultado puede persistirse en el archivo:

blockchain/datos_cadena.json

La documentación completa se encuentra en:

docs/06_blockchain.md

# 📚 Documentación del proyecto

Todo el desarrollo fue documentado durante la implementación para facilitar el mantenimiento y la comprensión del proyecto.

Los documentos disponibles son:

| Documento                     | Contenido                                                |
| ----------------------------- | -------------------------------------------------------- |
| `01_vision_proyecto.md`       | Objetivos, alcance y contexto del proyecto.              |
| `02_arquitectura.md`          | Arquitectura general del sistema y flujo de datos.       |
| `03_docker.md`                | Uso de Docker y administración del entorno de ejecución. |
| `04_base_de_datos.md`         | Modelo relacional y estructura de la base de datos.      |
| `05_etl.md`                   | Procesos ETL y carga de información.                     |
| `06_blockchain.md`            | Implementación de la blockchain y pruebas realizadas.    |
| `08_bitacora.md`              | Registro cronológico del desarrollo del proyecto.        |
| `09_comandos.md`              | Comandos utilizados durante el desarrollo.               |
| `10_consultas_productivas.md` | Consultas SQL implementadas y su propósito.              |


# Estructura del proyecto

AgroChain/
│
├── blockchain/              # Implementación de la blockchain
│   ├── bloque.py
│   ├── cadena.py
│   ├── prueba_bloque.py
│   ├── prueba_cadena.py
│   ├── cargar_bloques_productivos.py
│   └── datos_cadena.json
│
├── datasets/
│   └── raw/                 # Datasets originales
│
├── docs/                    # Documentación técnica
│
├── etl/                     # Procesos ETL
│
├── sql/
│   ├── queries/
│   └── schemas/
│
├── .env
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore

La organización modular facilita el mantenimiento del proyecto, la incorporación de nuevos procesos ETL, la ampliación de la base de datos y la integración futura con aplicaciones web, APIs o herramientas de análisis.


# Próximas mejoras

AgroChain fue desarrollado como un **Producto Mínimo Viable (MVP)** con una arquitectura modular que facilita su evolución. A partir de la base implementada, el proyecto puede ampliarse incorporando nuevas funcionalidades.

## Mejoras funcionales

* Incorporar nuevos cultivos además del maní (soja, maíz, trigo, girasol, entre otros).
* Agregar nuevos datasets provenientes de organismos oficiales como INTA o la Secretaría de Agricultura.
* Automatizar la actualización periódica de la información productiva.

## Mejoras en el proceso ETL

* Validación automática de calidad de datos antes de la carga.
* Registro de errores y generación de bitácoras automáticas.
* Programación de cargas periódicas mediante tareas automatizadas.
* Incorporación de nuevos procesos ETL reutilizando la arquitectura existente.

## Mejoras en la base de datos

* Optimización mediante índices para consultas de mayor volumen.
* Incorporación de nuevas tablas relacionadas con campañas agrícolas, variedades, clima y suelos.
* Implementación de procedimientos almacenados y vistas para consultas frecuentes.

## Mejoras en Blockchain

* Incorporar firma digital de los bloques.
* Persistir automáticamente la cadena después de cada actualización.
* Registrar eventos de auditoría sobre modificaciones realizadas en los datos.
* Evaluar la integración con plataformas blockchain de uso productivo para escenarios de trazabilidad distribuida.


## Visualización y análisis

* Desarrollo de un dashboard interactivo para consultar indicadores productivos.
* Incorporación de gráficos y mapas temáticos.
* Visualización de la evolución histórica de la producción por provincia y departamento.


## Integración con IoT

Una posible evolución del proyecto consiste en integrar AgroChain con dispositivos IoT para registrar automáticamente información proveniente del campo, por ejemplo:

* sensores de humedad del suelo,
* temperatura ambiente,
* precipitaciones,
* niveles de agua,
* variables de producción.

Estos datos podrían almacenarse en la base de datos y registrarse en la blockchain para fortalecer la trazabilidad de la información.

## API y aplicaciones

Como evolución del sistema, AgroChain podría incorporar una API REST para permitir que aplicaciones web o móviles consulten la información almacenada y registren nuevos eventos productivos de manera segura.


# Estado del proyecto

La versión actual de AgroChain implementa satisfactoriamente los objetivos definidos para el Producto Mínimo Viable (MVP):

* Infraestructura reproducible mediante Docker.
* Base de datos relacional en MySQL.
* Procesos ETL para la carga de datos históricos.
* Consultas SQL para el análisis de la producción.
* Blockchain simplificada para demostrar la trazabilidad de registros agrícolas.
* Documentación técnica completa para facilitar la instalación, comprensión y mantenimiento del proyecto.

Esta arquitectura constituye una base sólida para futuras ampliaciones orientadas al análisis de datos, la trazabilidad agropecuaria y la integración con nuevas tecnologías.




