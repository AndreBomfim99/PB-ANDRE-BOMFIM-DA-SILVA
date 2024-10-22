FROM editora x

JOIN livro y ON x.codeditora = y.editora
GROUP BY x.codeditora, x.nome
ORDER BY QuantidadeLivros DESC
LIMIT 5;