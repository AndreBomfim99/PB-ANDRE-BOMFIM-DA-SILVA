SELECT DISTINCT id_csv AS id, titulo_original_csv AS titulo, 'Filme' AS tipo, MAX(COALESCE(vote_count_tmdb, 0)) AS vote_count
FROM tab_movies_comum
WHERE COALESCE(genero_csv, '') LIKE '%Drama%' OR COALESCE(genero_csv, '') LIKE '%Romance%'
GROUP BY id_csv, titulo_original_csv
UNION ALL
SELECT DISTINCT id_csv AS id, titulo_original_csv AS titulo, 'Série' AS tipo, MAX(COALESCE(vote_count_tmdb, 0)) AS vote_count
FROM tab_series_comum
WHERE COALESCE(genero_csv, '') LIKE '%Drama%' OR COALESCE(genero_csv, '') LIKE '%Romance%'
GROUP BY id_csv, titulo_original_csv
ORDER BY vote_count DESC
LIMIT 10;