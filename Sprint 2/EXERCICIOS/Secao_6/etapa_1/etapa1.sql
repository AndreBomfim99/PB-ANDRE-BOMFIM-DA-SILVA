SELECT x.cod AS codlivro,
        x.titulo AS titulo,
         y.codautor AS codautor,
         y.nome AS nomeautor,
         x.valor AS valor,
        z.codeditora AS codeditora,
        z.nome AS nomeeditora
FROM livro x

JOIN autor y ON x.autor = y.codautor
JOIN editora z ON x.editora = z.codeditora
ORDER BY x.valor DESC
LIMIT 10;