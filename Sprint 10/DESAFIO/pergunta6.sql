SELECT 'Filme' AS tipo, AVG(DISTINCT COALESCE(popularity_tmdb, 0)) AS popularidade_media
FROM tab_movies_comum
WHERE COALESCE(genero_csv, '') LIKE '%Drama%' OR COALESCE(genero_csv, '') LIKE '%Romance%'
UNION ALL
SELECT 'Série' AS tipo, AVG(DISTINCT COALESCE(popularity_tmdb, 0)) AS popularidade_media
FROM tab_series_comum
WHERE COALESCE(genero_csv, '') LIKE '%Drama%' OR COALESCE(genero_csv, '') LIKE '%Romance%';