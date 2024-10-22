--E04 Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

SELECT 
    autor.nome AS nome,
    autor.codautor AS codautor,
    autor.nascimento AS nascimento,
    COUNT(livro.cod) AS quantidade
    
FROM 
    autor
LEFT JOIN 
    livro ON autor.codautor = livro.autor
    
GROUP BY 
    autor.codautor, autor.nome, autor.nascimento
    
ORDER BY 
    autor.nome ASC;
