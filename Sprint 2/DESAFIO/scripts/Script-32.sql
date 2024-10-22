-- Script para criar a tabela fato

CREATE TABLE fato_locacao (
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
    FOREIGN KEY (idCliente) REFERENCES dimensao_cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES dimensao_carro(idCarro),
    FOREIGN KEY (idcombustivel) REFERENCES dimensao_combustivel(idcombustivel),
    FOREIGN KEY (idVendedor) REFERENCES dimensao_vendedor(idVendedor)
);
