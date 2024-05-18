-- script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, COALESCE(split, 0) - formed AS lifespan
FROM metal_bands
WHERE split <= 2022 AND formed <= 2022 AND style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
