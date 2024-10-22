SELECT idCarro, COUNT(*) 
FROM tb_locacao 
GROUP BY idCarro 
HAVING COUNT(*) > 1;
