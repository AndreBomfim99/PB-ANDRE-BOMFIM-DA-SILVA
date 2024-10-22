--Script para criar a uma nova tabela tb_locacao_normalizada

CREATE TABLE tb_locacao_normalizada (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idcombustivel INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro),
    FOREIGN KEY (idcombustivel) REFERENCES tb_combustivel(idcombustivel),
    FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
);
