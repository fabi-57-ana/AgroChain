-- ==========================================================
-- Proyecto: AgroChain
-- Archivo : 01_schema.sql
-- Autor   : Equipo AgroChain
--
-- Descripción:
-- Crea toda la estructura de la Base de Datos.
--
-- Este archivo puede ejecutarse desde cero cuantas veces sea
-- necesario después de recrear el contenedor Docker.
-- ==========================================================

USE agrochain;

-- ==========================================================
-- TABLA: PRODUCCION_ANUAL
-- Dataset anual (98 registros)
-- ==========================================================

CREATE TABLE produccion_anual (

    id INT AUTO_INCREMENT PRIMARY KEY,

    anio INT NOT NULL,

    superficie_sembrada_ha INT,

    superficie_cosechada_ha INT,

    produccion_tn DECIMAL(12,2),

    rendimiento_kg_ha DECIMAL(10,2)

);

-- ==========================================================
-- TABLA: PROVINCIA
-- Catálogo único de provincias
-- ==========================================================

CREATE TABLE provincia (

    id INT AUTO_INCREMENT PRIMARY KEY,

    provincia_id_dataset INT,

    nombre VARCHAR(100) NOT NULL

);

-- ==========================================================
-- TABLA: DEPARTAMENTO
-- Catálogo único de departamentos
-- ==========================================================

CREATE TABLE departamento (

    id INT AUTO_INCREMENT PRIMARY KEY,

    departamento_id_dataset INT,

    nombre VARCHAR(150),

    provincia_id INT,

    FOREIGN KEY (provincia_id)
        REFERENCES provincia(id)

);

-- ==========================================================
-- TABLA: PRODUCCION_DEPARTAMENTO
-- Dataset histórico (5257 registros)
-- ==========================================================

CREATE TABLE produccion_departamento (

    id INT AUTO_INCREMENT PRIMARY KEY,

    anio INT NOT NULL,

    campania VARCHAR(20),

    departamento_id INT,

    superficie_sembrada_ha DECIMAL(12,2),

    superficie_cosechada_ha DECIMAL(12,2),

    produccion_tn DECIMAL(12,2),

    rendimiento_kg_ha DECIMAL(10,2),

    FOREIGN KEY (departamento_id)
        REFERENCES departamento(id)

);