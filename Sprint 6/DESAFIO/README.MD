# DESAFIO SPRINT 6

### O objetivo do desafio da Sprint 6 refere-se a entrega 1 de um desafio maior composto de outras 5 entregas. Nesta entrega 1 farei uma ingestão batch de dois arquivos CSV em em um bucket S3 em uma RAW Zone. Ou seja, criarei um processo automatizado que implementa uma pipeline para carregar arquivos CSV da minha máquina para um bucket S3, também criado automaticamente por código, em sua forma bruta (RAW Zone), utilizando Python para implementar e gerenciar a lógica, e Docker para empacotar e executar o código em um ambiente isolado. A biblioteca boto3 será usada para interagir logando na minha conta AWS durante o envio dos dados.

# ETAPA 1: Definição das perguntas que serão motivo de minha análise

### Analisando as duas bases de dados, moveis.csv e series.csv, elaborei um plano para seguir. Fiz muitas perguntas para que eu possa ter margem de "manobra", ou seja, não vou usar todas essas perguntas, mas penso que é um bom plano fazer muitas perguntas para que com o decorrer da análise eu possa decidir qual é mais viável, menos trabalhosa ou que tenha a resposta mais pertinente, assim não terei o retrabalho de voltar nesta etapa em um momento posterior. j

### Minha análise será sobre filmes e séries de Drama e Romance

### 1. Comparar o desempenho de Drama/Romance em Filmes vs. Séries
### Objetivo: determinar se Drama/Romance têm melhor desempenho em filmes ou séries.
### Como vou fazer: 
    • Nota Média (notaMedia): Avaliação das pessoas.
    • Popularidade (popularity): dado fornecido pela API TMDB.
    • Número de Votos (numeroVotos): Engajamento do público.
    • Enriquecer os dados usando a API TMDB para coletar métricas como popularidade, orçamento e receita.
    • Calcular médias por métrica: comparar a média de cada métrica entre filmes e séries.

### 2. Análise de Orçamento, Retorno e Popularidade
### Objetivo: vou identificar filmes e séries com:
    • Grande orçamento, mas baixo retorno financeiro e baixa popularidade.
    • Baixo orçamento, mas alto retorno financeiro e alta popularidade.
### Como vou fazer isso: 
    • Orçamento (budget): dado fornecido pela API TMDB.
    • Receita (revenue): Também fornecida pela API.
    • Popularidade (popularity): Métrica de engajamento.
    • Cálculo do ROI: O ROI é o retorno sobre investimento 

# ETAPA 2: Contrução do código python `envia.py`

## Etapa 2.1: Método para logar na conta AWS

#### Ao planejar a execução do desafio eu preciso logar na minha conta da AWS. Para facilitar e garantir o acesso, tendo em mente a segurança, utilizei um arquivo .env onde estão minhas credenciais. Ele é um arquivo simples de texto mas é mais fácil de trabalhar que um simples arquivo .txt. Meu script python irá acessar esse arquivo para logar na conta AWS. 

![imagem01](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img01.png)

## Etapa 2.2: Construção do script envia.py

#### - No cabeçalho do código, Com boto3 eu uso a bilbioteca boto3 para interagir com os serviços da AWS.  Neste contexto vou usar para criar buckets, fazer o upload. O os é um módulo para que eu possa fazer a lógica de interagir com o arquivo .env e me logar na AWS.

#### - `datetime` serve para que eu consiga fazer o bucket no formato conforme pedido no desafio:           `S3:\\data-lake-do-fulano \Raw\Local\CSV\Movies\2022\05\02\movies.csv`

#### - `ClientError` é uma classe que vem de boto3, como estou interagindo com a cloud, alguns erros ficam inperceptíveis, ou muito difíceis de saber o que está acontecendo. Essa classe ajuda a criar avisos para deixar bem nítido o que ocorre, me guiando na execução do código

![imagem02](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img02.png)

## Etapa 2.3: Função carregar_credenciais

#### A função carregar_credenciais vai fazer a lógica para logar na minha conta AWS com minhas credenciais que estão no arquivo .env, assim evito o “hardcoded” e torno o código mais seguro  (colocadas diretamente no código). Nos “ifs” eu uso os avisos do ClientError. 

![imagem03](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img03.png)

## Etapa 2.4: Função criar_bucket

#### A função criar_bucket verifica se meu bucket S3 já existe. Se existe, o bucket fica do jeito que está, se não existir, ele cria o bucket. Como o desafio dá a entender que vou reutilizar esse bucket, é importante essa lógica de verificação para não ter conflito. A base de tudo é o s3_client.head_bucket(Bucket=bucket_name), que faz a solicitação no S3 para verificar a existência do bucket. Ele retorna se o bucket for acessível, ou usa os alertas de ClientError caso tenha algum problema. Se tudo ocorrer bem, ele usa s3_client.create_bucket(Bucket=bucket_name, **bucket_config)  para criar o bucket.

![imagem04](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img04.png)

## Etapa 2.5: Função carregar_para_s3

#### a função carregar_para_s3 faz upload dos csvs da minha máquina para o bucket no S3. O parâmetro s3_client é fundamental para realizar a interação com o S3. Os outros parâmetros tem nomes intuitivos para seus usos.

#### Com data_atual = datetime.now() e caminho_s3 = f"{camada}/{origem}/{formato}/{especificacao}/{data_atual.year}/{data_atual.month:02}/{data_atual.day:02}/{nome_arquivo}" eu formato o bucket no formato S3:\\data-lake-andre-bomfim\Raw\Local\CSV\Movies\ano atual\mês atual\dia atual\movies.csv conforme instruído no desafio.

#### O s3_client.upload_file(arquivo_csv, bucket, caminho_s3) faz o upload do arquivo csv no caso (arquivo_csv) para o bucket no caminho definido (caminho_s3). O raise é apenas para relançar a exceção para quando o programa o chamar. 

![imagem05](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img05.png)

## Etapa 2.6: Restante do código e implementações

####  O restante do código verifica se os arquivos movies.csv e series.csv existem localmente, loga na minha conta AWS usando minhas credenciais que foram carregadas como um cliente S3. Garanto que o bucket data-lake-andre-bomfim exista e realiza o upload dos arquivos para o S3, organizo tudo por hierarquia definida nos parâmetros como Raw, Local, e a data atual. Caso um arquivo não seja encontrado, o programa me avisa lançando um erro. 

![imagem06](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img06.png)

# ETAPA 3 - Criação do container e do volume Docker 

## Etapa 3.1 Container Docker

#### Crio o arquivo dockerfile usando o python 3.8 para garantir que não tenha conflito de verões antigas e novas. com copy eu copio os arquivos envia.py. Movies.csv e series.csv para o diretório do container(/app). Ele também executa o comando pip install boto3 durante a construção da imagem para instalar a biblioteca Boto3, necessária para interagir com os serviços AWS. Ele que vai execurar o envia.py

![imagem07](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img07.png)

## Etapa 3.2 Volume Docker

#### Para a criação do volume usei Docker Compose, assim já automatizo a criação e execução de um container Docker para rodar o script Python envia.py e o volume com uma única chamada. Assim fica mais prático de organizar tudo. 

#### Explicando o principao do código:

        ◦ Build: Usa o Dockerfile que já está na pasta para construir a imagem.
        ◦ Container Name: Nomeia o meu container como container_andre_bomfim.
        ◦ Volumes: Monta o volume chamado volume_andre_bomfim na pasta /data dentro do container.
        ◦ Environment: Passa credenciais AWS como variáveis de ambiente a partir de valores no arquivo .env ou do sistema.
        ◦ Command: Copia os arquivos movies.csv e series.csv para o volume montado e, em seguida, executa o script envia.py.
    
#### Quero deixar claro que apenas nesse caso, destsa sprint, é uma boa solução usar Docker Compose, pois tenho ambiente simples com apenas um container, meu script envia.py faz o envio diretamente para o S3, ou seja, posso configurar tudo incluindo variáveis de ambiente, volumes e execução do script tudo nesse único arquivo docker-compose.yml.

#### Em outros casos, como por exemplo produção em larga escala, eu não poderia usar Docker Compose, pois ele tem suas limitações. Numa situação onde tivesse mais containeres eu não poderia usar o  Docker Compose, pois ele não é bom com gerenciamento distribuído. Existem outros casos também que não cabe descrever aqui para não me alongar demais. Mas nesses casos eu usaria um Docker Swarm ou até mesmo kubernetes. 

#### Achei bom deixar claro esse detalhe para mostrar que tenho consciência do que estou fazendo e que estudei a melhor solução para cada problema.

![imagem08](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img08.png)

# Etapa 4 Execução e finalização

## Etapa 4.1 Chamando o docker compose

####  Com o script python envia.py, o arquivo Dockerfile e o docker-compose.yml prontos, vou executar o docker-compose para dar início ao envio para o S3.

#### `docker-compose up –build`

#### Com essa única linha de comando eu executo todo o processo pedido no desafio. E como a imagem abaixo mostra, o comando construiu a imagem Docker, executou o container_andre_bomfim e durante a execução, o script envia.py criou o bucket data-lake-andre-bomfim no S3 e enviou os arquivos movies.csv e series.csv para o RAW.

![imagem09](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img09.png)

## Etapa 4.2 Evidências no S3

#### Evidência que o bucket data-lake-andre-bomfim foi criado com sucesso, o RAW foi criado conforme padrão pedido no desafio, e os arquivos csv foram enviados corretamente.

![imagem11](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img11.png)

## Etapa 4.3 Evidência da copia e envio dos CSVs para dentro do volume Docker

#### Evidência que o volume Docker foi criado e acessando o mesmo, podemos conferir os arquivos movies.csv e series.csv dentro dele. 

![imagem12](/Sprint%206/EVIDENCIAS/EVIDENCIA_DESAFIO/img12.png)

# Etapa 5 Conclusão

#### Entregas do desafio da Sprint 6

#### Questões baseadas no database: Entregue (presente neste documento na Etapa 1)

#### Código Python utilizando boto3 que cria um bucket no formato pedido e ainda envia arquivos CSV para o mesmo: Entregue ([envia.py](/Sprint%206/DESAFIO/envia.py))

#### Arquivo da imagem docker do container Docker: Entregue ([Dockerfile](/Sprint%206/DESAFIO/Dockerfile))

#### Arquivo do Docker Compose: Entregue ([Docker Compose](/Sprint%206/DESAFIO/docker-compose.yml))

#### Diante de tudo exposto no presente documento, dou por entregue e finalizado o desafio da Sprint 6.

























