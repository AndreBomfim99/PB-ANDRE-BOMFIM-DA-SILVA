# DESAFIO SPRINT 4

### O objetivo do desafio da Sprint 4 é utilizar os conhecimentos que adquiri nos cursos de Python e Docker, combinando-os para criar ambientes isolados no Docker (containeres) onde vou encapsular e executar scripts python.   

# Etapa 1: Preparação

### Etap a1.1: Seguindo boas práticas de organização de arquivos, criei uma pasta no diretório raiz "desafio_sprint_4" de forma a deixar bem ordenados meus arquivos. Em seguida baixei e inseri o script "carguru.py".

![Imagem 0](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img00.png)

### Etapa 1.2: Neste desafio utilizarei o VS Code, portanto, instalei a extensão "Docker" de forma a facilitar o gerenciamento e desenvolvimento de containers e imagens diretamente nele.  

![Imagem 1](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img01.png)

### Etapa 1.3: Instalei e iniciei o Docker. A imagem abaixo é apenas para mostrar ele rodando em segundo plano no sistema.

![Imagem 2](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img02.png)

# Etapa 2: EXECUÇÃO

### Etapa 2.1: Comecei o desafio estudando o que era o arquivo carguru.py, fiz a execução e obtive o resultado abaixo. Esse script gera dados aleatórios, onde escolhe aleatoriamente um carro da lista de carros e mostra uma mensagem com esse carro.  

![Imagem 3](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img03.png)

### Etapa 2.2: Em seguida verifiquei se já existiam containers no meu sistema. Utilizei o comando `docker ps -a` que retorna todos os containers, incluindo os que estão parados. A imagem abaixo mostra que nenhum container foi criado.

![Imagem 4](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img04.png)

### Etapa 2.3: Aqui começo a criar a imagem Docker. Como terei que criar duas imagens Docker, para organizar os arquivos e não terem conflito de nomes, nomeei cada imagem de acordo com o arquivo que ela executará. Este que criei a seguir será o Dockerfile.carguru. Ele vai empacotar o script, garantindo que rode em qualquer sistema operacional onde o container for executado. Código explicado:

**`FROM python:3.9-slim`**: usei o python 3.9-slim pois foi o que melhor funcionou sem sobrecarregar meu computador. 

**`WORKDIR /app`**: cria a pasta de trabalho `/app` no container. 

**`COPY carguru.py .`**: copia o arquivo `carguru.py` para o pasta `/app` dentro do container. 

**`CMD ["python", "carguru.py"]`**: aqui defino o comando que será executado quando o container iniciar, essa linha configura a execução do script como o processo principal do container.

![Imagem 5](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img05.png)

### Etapa 2.4: Agora vou construir a imagem Docker. Para isso usei o comando `docker build -f Dockerfile.carguru -t carguru_imagem .`, que faz a construção de uma imagem com o nome ou tag de "carguru_imagem" usando um Dockerfile específico.

![Imagem 6](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img06.png)

### Etapa 2.5: A imagem abaixo mostra que a imagem carguru_imagem foi criada e nomeada corretamente. 

![Imagem 7](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img07.png)

### Etapa 2.6: O próximo passo é rodar o container. Para iniciá-lo, uso o comando `docker run --name carguru-container carguru_imagem`. Esse comando cria um container chamado carguru-container a partir da imagem carguru_imagem. A saída do container indica que ele está funcionando corretamente, pois executou o script "carguru.py".

![Imagem 8](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img08.png)

### Etapa 2.7: Verifico novamente o status dos constainer do Docker com o comando `docker ps -a`. Com ele vejo que exatamento o que descrevi na Etapa 2.6: que o container carguru-container foi executado a partir da imagem carguru_imagem com o comando python carguru.py, mas ele saiu com o status Exited (0). Essa informação do status é muito importante, pois isso indica que o script carguru.py foi executado com sucesso e o código de saída em "0" ali mostra que terminou sem erros também, ou seja, ele foi executado e depois finalizado, o que indica que ele pode ser reutilizado.

![Imagem 9](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img09.png)

### Etapa 2.8: Como mostrado na imagem anterior, o container está parado. Para reiniciá-lo eu poderia apenas usar `docker restart carguru-container`, mas o resultado não seria perceptível, pois seria apenas um aviso no terminal de que ele foi inicializado. A imagem abaixo mostra isso:

![Imagem 9a](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img09a.png)

### Para provar de maneira mais categórica que posso reutilizá-lo, vou usar  `docker start -a carguru-container`, onde posso demonstrar o container interagindo com o script com o  resultado do script sendo mostrado no terminal. O -a é de "attach", ele faz com que o terminal exiba a saída do container enquanto ele está em execução. 

### Obs.: Esse comando só pode ser usado unicamente porque tenho certeza que o container está parado. Se eu não estivesse certo disso, eu teria que usar obrigatoriamente `docker restart carguru-container`, pois esse comando força o container a parar caso ele ainda esteja em execução e assim o reinicia.

![Imagem 10](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img10.png)

### Etapa 2.9: Criando o código do script conforme pedido no "item 4.3 Etapa 3" do documento do desafio

### Meu código utiliza a biblioteca hashlib para criar uma máscara (hash) da entrada fornecida pelo usuário. A função que irei usar dessa biblioteca é a SHA-1, que gera um hash de 160 bits.

### Criei um while com um loop, que só é interrompido quando digitar "sair".

### A entrada é convertida usando entrada.encode() e passada para hashlib.sha1() para gerar o hash SHA-1. Com hexdigest() converto o hash  gerado para uma representação hexadecimal.

![Imagem 11](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img11.png)

### Etapa 2.10: Crio a segunda imagem Docker, usando a mesma lógica de organização que fiz com a primeira. Ela é exatamente igual a primeira, mas mudo os scripts que ela irá executar nas linhas 5 e 6.

![Imagem 12](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img12.png)

### Etapa 2.11: Com o comando `docker build -f Dockerfile.mascarar -t mascarar-dados . ` construo a segunda imagem de nome "mascarar-dados". A imagem abaixo mostra o resultado bem sucedido do comando.

![Imagem 13](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img13.png)

### Etapa 2.12: Inicio o container com `docker run --name mascarar-container mascarar-dados` e o nomeio como mascarar-container. Ele executa corretamente o script `mascarar.py`. 

![Imagem 14](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img14.png)

### Etapa 2.13: Digito uma frase qualquer para que o script possa fazer o mascaramento.

![Imagem 15](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img15.png)

### Etapa 2.14: Mascaramento bem sucedido.

![Imagem 16](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img16.png)

### Etapa 2.15: Ao digitar "sair" o script encerra. 

![Imagem 17](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img17.png)

### Etapa 2.16: Para finalizar, as imagens abaixo mostram que os containeres rodaram e finalizaram sem erros. Execução bem sucedida.

![Imagem 18](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img18.png)

![Imagem 19](/Sprint%204/EVIDENCIAS/EVIDENCIAS_DESAFIO/img19.png)

# Etapa 3: ITENS EXECUTADOS E ENTREGAS

### Esse desafio é dividido em 3 etapas no item 4 do documento que descreve o desafio. Vou inserí-las aqui e aproveitar para mostrar os itens que executei e minhas entregas.

### Etapa 3.1: Itens executados

- 4.1. Etapa 1: Construa uma imagem a partir de um arquivo de instruções Dockerfile que execute o código carguru.py Após, execute um container a partir da imagem criada.

- RESPOSTA: Da Etapa 2.3 até a Etapa 2.7 mostro toda a execução. Portanto este item está entregue.

- 4.2. Etapa 2: É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.

- RESPOSTA: Na Etapa 2.8 provo que é possível sim reutilizar containeres. As respostas a esses questionamentos estão melhor explicadas no arquivo [QUESTIONAMENTOS](/Sprint%204/DESAFIO/QUESTIONAMENTOS.MD). Portanto este item está entregue.

- 4.3. Etapa 3: Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução. Abaixo seguem as instruções.

    1. Criar novo script Python que implementa o algoritmo a seguir:

         • Receber uma string via input.

         • Gerar o hash da string por meio do algoritmo SHA-1.

         • Imprimir o hash em tela, utilizando o método hexdigest.

         • Retornar ao passo 1.

    - RESPOSTA: na Etapa 2.9 mostro meu código, o qual segui exatamente esses passos do algoritmo explicitado. Portanto este item está entregue.

    2. Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente.

    - RESPOSTA: Nas Etapas 2.10 e 2.11 mostro o código e a execução. Portanto este item está entregue.

    3. Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento.

    - RESPOSTA: Da Etapa 2.12 até a Etapa 2.15 executo este item sendo executado. Portanto este item está entregue.


### Etapa 3.2: Entregas exigidas no item 2 do documento do desafio

1. Arquivo Dockerfile: 

- Resposta: [Dockerfile.carguru](/Sprint%204/DESAFIO/DESAFIO/Dockerfile.carguru) e [Dockerfile.mascarar](/Sprint%204/DESAFIO/DESAFIO/Dockerfile.mascarar)

- Script python de mascaramento Hash

- Resposta: [Script de mascaramento Hash](/Sprint%204/DESAFIO/DESAFIO/mascarar.py)

2. Comandos utilizados para execução do container

- Resposta:

- `docker build -f Dockerfile.carguru -t carguru_imagem .`

- `docker run --name carguru-container carguru_imagem`

- `docker start -a carguru-container`

- `docker build -f Dockerfile.mascarar -t mascarar-dados .` 

- `docker run --name mascarar-container mascarar-dados`

3. Respostas para os questionamentos no formato Markdown.

- Reposta: [QUESTIONAMENTOS](/Sprint%204/DESAFIO/QUESTIONAMENTOS.MD)

4. Evidências (prints de tela) da execução bem sucedida.

- Resposta: todas presentes neste documento.

#### Diante de tudo exposto no presente documento, dou por finalizado o desafio da Sprint 4.
 









