-- script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans

SELECT origin, NOT UNIQUE(fans) AS nb_fans
FROM metal_bands;
