# AgroChain - Comandos utilizados


## 1. Comandos Docker


| Comando                                  | Entorno    | Descripción                                               |
|------------------------------------------|------------|-----------------------------------------------------------|
| `docker ps`                              | PowerShell | Ver contenedores actualmente en ejecución.                |
| `docker ps -a`                           | PowerShell | Ver todos los contenedores, incluyendo los detenidos.     |
| `docker compose up -d`                   | PowerShell | Crear e iniciar los servicios definidos en Docker Compose.|
| `docker compose up -d --force-recreate`  | PowerShell | Recrear los contenedores aunque ya existan.               |
| `docker compose down`                    | PowerShell | Detener y eliminar los contenedores del proyecto. No      |elimina los datos del volumen.             |            |                                                          
| `docker stop agrochain-mysql`            | PowerShell | Detener manualmente el contenedor MySQL.                  |
| `docker volume rm agrochain_mysql_data`  | PowerShell | Eliminar el volumen de datos. Borra completamente la  información almacenada en MySQL.           |            |                                                           |
| `docker exec -it agrochain-mysql mysql -u root -p`    | PowerShell | Acceder al cliente MySQL dentro del     contenedor.                                                                                                         |


## 2. Comandos MySQL


| Comando                | Entorno | Descripción                                |
|------------------------|---------|--------------------------------------------|
| `SHOW DATABASES;`      | MySQL   | Mostrar las bases de datos disponibles.    |
| `USE agrochain;`       | MySQL   | Seleccionar la base de datos del proyecto. |
| `SHOW TABLES;`         | MySQL   | Mostrar las tablas existentes.             |
| `SELECT * FROM tabla;` | MySQL   | Consultar registros de una tabla.          |
| `exit;`                | MySQL   | Salir del cliente MySQL.                   |
| `\c`                   | MySQL   | Cancelar el comando SQL actual.            |

## 3. Consultas productivas realizadas

| Consulta                                | Objetivo                                                            |
|-----------------------------------------|---------------------------------------------------------------------|
| Evolución histórica de producción anual | Analizar el comportamiento del cultivo de maní entre 1927 y 2024.   |
| Producción por provincia año 2024       | Identificar las provincias con mayor producción.                    |
| Producción por departamento año 2024    | Identificar las principales zonas productoras.                      |
| Evolución desde el año 2000             | Observar el cambio productivo asociado a incorporación tecnológica. |
| Datos departamentales 2024              | Obtener registros utilizados para la prueba blockchain.             |


Ejemplo de resultado:

| Provincia           | Producción total (tn) |
|---------------------|----------------------:|
| Córdoba             | 1268363               |
| Buenos Aires        | 315761                |
| La Pampa            | 127986                |
| Santa Fe            | 51170                 |
| San Luis            | 36338                 |
| Tucumán             | 3899                  |
| Salta               | 2593                  |
| Catamarca           | 2280                  |
| Santiago del Estero | 627                   |
| Jujuy               | 520                   |


## 4. Situaciones particulares

### Detención manual del contenedor MySQL

Durante el desarrollo se utilizó:

docker stop agrochain-mysql