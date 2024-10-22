--E06 Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes. 

SELECT
    autor.codautor AS codautor,
    autor.nome AS nome,
    count (*) AS quantidade_publicacoes
FROM
    autor

LEFT JOIN
    livro ON autor.codautor = livro.autor

GROUP BY
    autor.codautor, autor.nascimento, autor.nome

ORDER BY
   quantidade_publicacoes DESC
LIMIT 1

