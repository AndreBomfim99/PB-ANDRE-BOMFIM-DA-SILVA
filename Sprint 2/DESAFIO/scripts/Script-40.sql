SELECT 
    y.marcaCarro, 
    y.modeloCarro, 
    x.valorLocacao, 
    x.dataLocacao
FROM 
    tb_locacao_normalizada x
JOIN 
    dimensao_carro y ON x.idCarro = y.idCarro
WHERE 
    x.valorLocacao > 200;
