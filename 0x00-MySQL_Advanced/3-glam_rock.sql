-- script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, COALESCE(split, 0) - COALESCE(formed, 0) AS lifespan
FROM metal_bands
GROUP BY band_name
ORDER BY lifespan DESC
WHERE split < 2022;
