-- E10 A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
--Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
--As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

SELECT
    vendedor.nmvdd AS vendedor,
    sum(vendas.qtd * vendas.vrunt) AS valor_total_vendas,
    round((sum(vendas.qtd * vendas.vrunt) * vendedor.perccomissao / 100), 2) AS comissao

FROM
    tbvendas AS vendas
JOIN
        tbvendedor AS vendedor
            ON vendas.cdvdd = vendedor.cdvdd

WHERE status = 'Concluído'

GROUP BY
    vendedor.nmvdd,
    vendedor.perccomissao

ORDER BY comissao DESC
