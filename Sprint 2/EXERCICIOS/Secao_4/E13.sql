--E13 Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  
--As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

SELECT  vendas.cdpro,
        vendas.nmcanalvendas,
        vendas.nmpro,
        SUM(vendas.qtd) AS quantidade_vendas
        
FROM    tbvendas as vendas

WHERE   vendas.status = 'Concluído'

GROUP BY vendas.cdpro, vendas.nmcanalvendas, vendas.nmpro

ORDER BY quantidade_vendas asc

LIMIT 10