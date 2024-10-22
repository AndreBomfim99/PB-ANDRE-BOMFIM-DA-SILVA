--E07 Apresente a query para listar o nome dos autores 
--com nenhuma publicação. Apresentá-los em ordem crescente.

SELECT 	autor.nome as nome

FROM	autor

LEFT JOIN
    	livro on autor.codautor = livro.autor

GROUP BY 
    	autor.codautor, autor.nascimento, autor.nome

HAVING 	ifnull(count(livro.cod), 0) = 0

ORDER BY autor.nome ASC

