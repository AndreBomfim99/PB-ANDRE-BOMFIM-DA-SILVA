SELECT 
    x.idLocacao, 
    comb.tipoCombustivel
FROM fato_locacao x
JOIN dimensao_combustivel comb ON x.idcombustivel = comb.idcombustivel;
