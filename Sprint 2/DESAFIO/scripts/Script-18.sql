--Script para popular a tabela tb_locacao_normalizada

INSERT INTO tb_locacao_normalizada (
    idLocacao, idCliente, idCarro, idcombustivel, idVendedor, 
    dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
)
SELECT idLocacao, idCliente, idCarro, idcombustivel, idVendedor, 
       dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao;
