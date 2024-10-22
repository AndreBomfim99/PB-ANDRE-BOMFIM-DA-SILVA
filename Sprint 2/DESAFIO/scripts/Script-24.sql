SELECT idCliente, COUNT(*) 
FROM tb_locacao 
GROUP BY idCliente 
HAVING COUNT(*) > 1;
