--E12 Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
--Observação: Apenas vendas com status concluído.

--vendedorMV = vendedor do Menor Valor

WITH vendedorMV AS (
   
SELECT  vdr.cdvdd,
         SUM(vds.qtd * vds.vrunt) AS valor_total_vendas

FROM    tbvendedor vdr

LEFT JOIN
        tbvendas vds ON vdr.cdvdd = vds.cdvdd
WHERE
        vds.status = 'Concluído'
GROUP BY
        vdr.cdvdd
ORDER BY
        valor_total_vendas ASC
LIMIT 1
)

SELECT  dep.cddep,
        dep.nmdep,
        dep.dtnasc,
        vnd.valor_total_vendas
        
FROM     tbdependente dep

INNER JOIN    vendedorMV vnd ON dep.cdvdd = vnd.cdvdd;