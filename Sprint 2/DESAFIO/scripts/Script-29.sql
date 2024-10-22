-- Inserção dos dados na tabela tb_carro selecionando o maior valor de kmCarro

INSERT INTO tb_carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT idCarro, MAX(kmCarro), MAX(classiCarro), MAX(marcaCarro), MAX(modeloCarro), MAX(anoCarro)
FROM tb_locacao
GROUP BY idCarro;

