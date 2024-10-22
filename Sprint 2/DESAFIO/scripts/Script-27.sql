-- REsolvendo o problema de duplicata sómente em tb_carro e tb_cliente

INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao
WHERE idCliente IN (
    SELECT MIN(idCliente)
    FROM tb_locacao
    GROUP BY idCliente
);

INSERT INTO tb_carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao
WHERE idCarro IN (
    SELECT MIN(idCarro)
    FROM tb_locacao
    GROUP BY idCarro
);
