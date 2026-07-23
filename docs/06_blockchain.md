# Blockchain - Registro de producción agrícola

## Objetivo

Implementar una primera prueba de integración entre los datos agrícolas almacenados en MySQL y una estructura blockchain básica.

El objetivo es demostrar cómo un registro productivo puede transformarse en un bloque con identidad propia mediante un hash, permitiendo verificar si la información fue modificada posteriormente.


## Alcance

En esta etapa no se realizará una carga completa de todos los registros históricos.

Se utilizarán pocos registros reales de producción de maní correspondientes al año 2024 para demostrar el funcionamiento de trazabilidad.


## Actividades realizadas

### Creación de estructura blockchain

Se implementaron:

- clase Bloque
- clase Blockchain
- bloque Genesis
- generación de hash
- enlace entre bloques mediante hash anterior
- validación de integridad de cadena


## Pruebas realizadas

Se realizaron dos pruebas:

### Cadena sin modificaciones

La validación de la cadena devuelve:


True


Confirmando que los bloques mantienen su integridad.


### Modificación manual de un bloque

Se modificó temporalmente un dato de producción dentro de un bloque.

Resultado:


False


La cadena detectó la alteración porque el hash calculado dejó de coincidir con el hash almacenado.


## Próximo paso

Crear un proceso para obtener registros productivos desde MySQL y generar bloques blockchain con información agrícola real.

## Integración con datos productivos reales


Se creó el proceso:


blockchain/cargar_bloques_productivos.py



El objetivo fue obtener registros reales almacenados en MySQL y transformarlos en bloques dentro de la cadena blockchain.


## Datos utilizados

Fuente:

Tabla:


produccion_departamento



Filtro aplicado:


Año 2024



Se seleccionaron los principales departamentos productores de maní para realizar una prueba de trazabilidad.


## Bloques generados


Se generaron:

- 1 bloque Genesis
- 5 bloques con información productiva real


Ejemplo de información registrada:
```text
{
 "cultivo": "mani",
 "anio": 2024,
 "provincia": "Córdoba",
 "departamento": "Río Cuarto",
 "produccion_tn": 297500,
 "rendimiento_kg_ha": 3500
}
```
Validación final

Resultado de la ejecución:

VALIDACION DE CADENA:
True

Esto confirma que los bloques mantienen su integridad y que cada registro está vinculado mediante el hash del bloque anterior.

Estado

Primera integración MySQL + Blockchain realizada correctamente.

## Persistencia de la cadena blockchain

Luego de validar la integridad de la cadena, se incorporó una etapa de persistencia.

El proceso genera el archivo:

blockchain/datos_cadena.json

Este archivo almacena:

- índice del bloque
- fecha de creación
- datos productivos registrados
- hash del bloque anterior
- hash propio del bloque


De esta forma, la información registrada no queda solamente en memoria durante la ejecución, sino que puede ser conservada y revisada posteriormente.

Resultado de la prueba:

VALIDACION DE CADENA:
True

Estado:

Cadena blockchain persistida correctamente.