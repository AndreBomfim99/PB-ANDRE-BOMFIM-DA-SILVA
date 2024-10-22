--E16 Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
--As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).
--Obs: Somente vendas concluídas.

SELECT 
    estado,
    nmpro,
    (SELECT ROUND(AVG(qtd), 4) 
     FROM tbvendas 
     WHERE status = 'Concluído' AND estado = v.estado AND nmpro = v.nmpro) AS quantidade_media
FROM 
    tbvendas v
WHERE 
    status = 'Concluído'
GROUP BY 
    estado, nmpro
ORDER BY 
    estado;

