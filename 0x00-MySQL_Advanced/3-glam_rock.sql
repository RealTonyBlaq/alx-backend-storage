-- script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, COALESCE(split, 0) - COALESCE(formed, 0) AS lifespan
FROM metal_bands
WHERE metal_bands.split <= 2022 AND metal_bands.formed <= 2022 AND LIKE '%Glam rock%'
ORDER BY lifespan DESC;
