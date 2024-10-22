--E11 Apresente a query para listar o código e nome cliente com maior gasto na loja. 
--As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.


SELECT
    vendas.cdcli as cdcli,
    vendas.nmcli,
    SUM(vendas.qtd * vendas.vrunt) AS gasto

FROM tbvendas AS vendas

JOIN tbvendedor AS vendedor

ON vendas.cdvdd = vendedor.cdvdd

WHERE status = 'Concluído'

GROUP BY vendas.cdcli, vendas.nmcli

ORDER BY gasto DESC

LIMIT 1