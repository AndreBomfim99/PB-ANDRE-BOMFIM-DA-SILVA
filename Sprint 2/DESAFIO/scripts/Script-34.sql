-- Mostrar o desempenho dos vendedores

SELECT 
    x.nomeVendedor, 
    COUNT(y.idLocacao) AS totalLocacoes, 
    SUM(y.qtdDiaria) AS totalDiarias
FROM fato_locacao y
JOIN dimensao_vendedor x ON y.idVendedor = x.idVendedor
GROUP BY x.nomeVendedor;