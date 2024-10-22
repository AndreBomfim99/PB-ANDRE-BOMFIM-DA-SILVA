--E08 Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
--e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.


SELECT
    vendedor.cdvdd,
    vendedor.nmvdd

FROM tbvendedor AS vendedor

LEFT JOIN tbvendas AS vendas

ON vendas.cdvdd = vendedor.cdvdd

WHERE vendas.status = 'Concluído'

ORDER BY vendas.status

LIMIT 1
