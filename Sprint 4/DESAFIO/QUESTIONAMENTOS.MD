# QUESTIONAMENTOS

## É possível reutilizar contêineres?
Sim, os contêineres docker podem ser iniciados, parados e reiniciados quando for necessário. Claro que existem casos onde isso é mais indicado (teste de aplicações) ou menos indicado (aplicações de segurança).

## Comandos para reiniciar contêineres

`docker restart <nome ou ID do container>` É usado para reiniciar um container, esteja ele parado ou em execução. Se o container já estiver em execução, o comando o força a parar e o inicia novamente. 

