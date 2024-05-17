-- script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans

SELECT origin, SUM(fans) AS nb_fans RANK() OVER (ORDER BY SUM(num_fans) DESC) AS country_rank
FROM metal_bands
GROUP BY origin;
