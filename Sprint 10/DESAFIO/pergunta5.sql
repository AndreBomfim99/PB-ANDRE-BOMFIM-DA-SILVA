SELECT nome_artista_csv AS ator, COUNT(DISTINCT id_csv) AS total_aparicoes, 'Filme' AS tipo
FROM tab_movies_comum
WHERE COALESCE(genero_csv, '') LIKE '%Drama%' OR COALESCE(genero_csv, '') LIKE '%Romance%'
GROUP BY nome_artista_csv
UNION ALL
SELECT nome_artista_csv AS ator, COUNT(DISTINCT id_csv) AS total_aparicoes, 'Série' AS tipo
FROM tab_series_comum
WHERE COALESCE(genero_csv, '') LIKE '%Drama%' OR COALESCE(genero_csv, '') LIKE '%Romance%'
GROUP BY nome_artista_csv
ORDER BY total_aparicoes DESC
LIMIT 10;