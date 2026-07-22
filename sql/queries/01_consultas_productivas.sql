-- ==========================================================
-- AgroChain
-- Consultas productivas sobre cultivo de maní
-- ==========================================================
--
-- Objetivo:
-- Generar consultas de análisis sobre la producción histórica
-- y obtener información que luego podrá utilizarse para
-- generar eventos trazables hacia blockchain.
--
-- Dataset:
-- Producción histórica de maní 1927-2024
--
-- ==========================================================


-- ==========================================================
-- CONSULTA 1
-- Evolución histórica de producción y rendimiento
--
-- Permite observar el comportamiento productivo del cultivo
-- a través del tiempo.
-- ==========================================================

SELECT
    anio,
    produccion_tn,
    rendimiento_kg_ha
FROM produccion_anual
ORDER BY anio;



-- ==========================================================
-- CONSULTA 2
-- Producción por provincia - última campaña disponible
--
-- Identifica la distribución territorial de la producción.
-- ==========================================================

SELECT
    p.nombre AS provincia,
    SUM(pd.produccion_tn) AS produccion_total_tn
FROM produccion_departamento pd

JOIN departamento d
    ON pd.departamento_id = d.id

JOIN provincia p
    ON d.provincia_id = p.id

WHERE pd.anio = 2024

GROUP BY p.nombre

ORDER BY produccion_total_tn DESC;



-- ==========================================================
-- CONSULTA 3
-- Ranking de departamentos productores
--
-- Identifica las principales zonas productivas.
-- ==========================================================

SELECT
    d.nombre AS departamento,
    p.nombre AS provincia,
    SUM(pd.produccion_tn) AS produccion_total_tn

FROM produccion_departamento pd

JOIN departamento d
    ON pd.departamento_id = d.id

JOIN provincia p
    ON d.provincia_id = p.id

WHERE pd.anio = 2024

GROUP BY
    d.nombre,
    p.nombre

ORDER BY produccion_total_tn DESC

LIMIT 10;



-- ==========================================================
-- CONSULTA 4
-- Evolución productiva período tecnológico
--
-- Se analiza el período posterior al año 2000,
-- donde se observa un cambio estructural en productividad.
-- ==========================================================

SELECT
    anio,
    produccion_tn,
    rendimiento_kg_ha
FROM produccion_anual

WHERE anio >= 2000

ORDER BY anio;



-- ==========================================================
-- CONSULTA 5
-- Evento productivo preparado para blockchain
--
-- Genera una salida estructurada con información productiva
-- territorial que posteriormente podrá transformarse en un
-- registro trazable.
-- ==========================================================

SELECT

    pd.anio,
    'mani' AS cultivo,
    p.nombre AS provincia,
    d.nombre AS departamento,
    pd.produccion_tn,
    pd.rendimiento_kg_ha

FROM produccion_departamento pd

JOIN departamento d
    ON pd.departamento_id = d.id

JOIN provincia p
    ON d.provincia_id = p.id

WHERE pd.anio = 2024

ORDER BY
    provincia,
    departamento;