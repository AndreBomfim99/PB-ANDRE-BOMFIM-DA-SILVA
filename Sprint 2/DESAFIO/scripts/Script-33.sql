-- Inserindo dados na tabela fato_locacao

INSERT INTO fato_locacao (idLocacao, idCliente, idCarro, idcombustivel, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idCarro, idcombustivel, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao_normalizada;
