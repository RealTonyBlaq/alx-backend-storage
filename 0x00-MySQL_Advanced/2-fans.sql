-- script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans

SELECT origin, RANK() OVER (ORDER BY SUM(fans) DESC) AS nb_fans
FROM metal_bands
GROUP BY origin;
