SELECT t.ano, COUNT(DISTINCT m.id_csv) AS total_lancamentos, 'Filme' AS tipo
FROM tab_movies_comum m
JOIN tab_tempo t ON m.ano_lancamento_csv = t.ano
WHERE COALESCE(genero_csv, '') LIKE '%Drama%' OR COALESCE(genero_csv, '') LIKE '%Romance%'
GROUP BY t.ano
UNION ALL
SELECT t.ano, COUNT(DISTINCT s.id_csv) AS total_lancamentos, 'Série' AS tipo
FROM tab_series_comum s
JOIN tab_tempo t ON s.ano_lancamento_csv = t.ano
WHERE COALESCE(genero_csv, '') LIKE '%Drama%' OR COALESCE(genero_csv, '') LIKE '%Romance%'
GROUP BY t.ano
ORDER BY total_lancamentos DESC