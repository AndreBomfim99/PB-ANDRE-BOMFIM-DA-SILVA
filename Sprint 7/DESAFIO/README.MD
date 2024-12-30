# DESAFIO SPRINT 7

### O objetivo do desafio da Sprint 7 é a execução da segunda etapa das 5 etapas que realizarei até  o final do programa. Essa etapa consiste em fazer a ingestão da API do TMDB via uma função Lambda, essa API vai complementar as informações contidas nos arquivos movies.csv e series.csv trabalhados na sprint anterior.

### As perguntas que elaborei na sprint anterior foram reformuladas. Pesquisei mais a fundo sobre o que a API do TMDB poderia oferecer, e como dados sobre receita e orçamento de séries não estão contidos nele, achei por bem eliminar por enquanto as perguntas que eu faria nesse sentido. Caso eu ache uma API ou database que supra essas informações, planejarei se posso voltar nesse assunto sem precisar refazer alguma etapa. As perguntas são:

### 1. Comparar o desempenho de Drama/Romance em Filmes vs. Séries
### Objetivo: determinar se Drama/Romance têm melhor desempenho em filmes ou séries.
### Como vou fazer: 
    • Nota Média (notaMedia): Avaliação das pessoas.
    • Popularidade (popularity): dado fornecido pela API TMDB.
    • Número de Votos (numeroVotos): Engajamento do público.
    • Calcular médias por métrica: comparar a média de cada métrica entre filmes e séries.

### Etapa 1: Por já ter feito exercício sobre Lambda na sprint anterior, sei que preciso de que o ambiente onde o script será executado, tenha suas dependências atendidas. Por isso acabei identificando esse detalhe aqui, ou seja, para executar o Lambda preciso das dependências do `tmdbv3api`. Comecei criando localmente um container Docker. Nesse container vou executar os comandos que preciso para executar essa parte da tarefa.

![imagem01](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img01.png)

### Etapa 2: Executei o build desse container

![imagem02](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img02.png)

### Etapa 3: Executei o comando para entrar no modo bash do container

![imagem03](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img03.png)

### Etapa 4: no modo bash contruí os diretórios necessários.

![imagem04](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img04.png)

### Etapa 5: Aqui faço a instalação do pacote do `tmdbv3api`

![imagem05](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img05.png)

### Etapa 6: Executo o zip de todos os arquivos 

![imagem07](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img07.png)

### Etapa 7: Copio o arquivo para minha maquina local

![imagem09](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img09.png)

### Etapa 8: Agora vou subir o arquivo `camadatmdbapi.zip`para meu bucket S3

![imagem10](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img10.png)

### Etapa 9: Agora no serviço Lambda, vou criar uma função

![imagem12](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img12.png)

### Etapa 10: Faço as configurações necessárias para criação da função

![imagem13](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img13.png)

### Etapa 11: Insiro meu código Lambda. Fiz uma execução prévia para achar mais erros, ele obviamente deu Failed. 

![imagem14](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img14.png)

### Etapa 12: Vou criar minha Layer para implementar o arquivo da biblioteca `tmdbv3api`

![imagem15](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img15.png)

### Etapa 13: Configurações obrigatórias da Layer

![imagem16](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img16.png)

### Etapa 14: Aqui escolho o arquivo para a Layer

![imagem18](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img18.png)

### Etapa 15: Como fiz executei previamente o código, o log de erros acusou também o tempo de timeout, então aproveito e faço a configuração do Timeout da função aqui

![imagem20](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img20.png)

### Etapa 16: Outro erro que o log acusou foi a permissão, então vou também configurá-la. 

![imagem21](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img21.png)

### Etapa 17: Crie uma policy específica para permitir que meu código acesse o meu bucket

![imagem24](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img24.png)

### Etapa 18: Executo novamente minha função Lambda. Dessa vez a execução é bem sucedida.

![imagem25a](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img25a.png)

### Etapa 19: O resultado final. Os arquivos JSON foram criados.

![imagem26](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img26.png)

### Etapa 12: Vou abrir o arquivo `movie-Drama-2022-1-055025.json` só a título de demonstração

![imagem27](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img27.png)

### Etapa 13: Arquivos produzidos no Desafio

Código [Dockerfile](/Sprint%207/DESAFIO/Dockerfile)

Código Python [meucodigo.py](/Sprint%207/DESAFIO/meucodigo.py)

Arquivo da depedência da biblioteca `tmdbv3api` [camada-tmbdapi.zip](/Sprint%207/DESAFIO/camada-tmbdapi.zip)

#### Diante de tudo exposto no presente documento, dou por entregue e finalizado o desafio da Sprint 7.































