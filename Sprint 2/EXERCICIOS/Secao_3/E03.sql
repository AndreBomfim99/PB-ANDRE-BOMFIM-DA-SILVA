--E03 Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente. 

SELECT  count(*) AS quantidade,
        editora.nome AS nome,
        endereco.estado AS estado,
        endereco.cidade AS cidade

FROM    livro

JOIN    editora ON livro.editora = editora.codeditora

JOIN    endereco ON editora.endereco = endereco.codendereco

GROUP BY editora.nome, endereco.estado, endereco.cidade

ORDER BY quantidade DESC

LIMIT 5;
    