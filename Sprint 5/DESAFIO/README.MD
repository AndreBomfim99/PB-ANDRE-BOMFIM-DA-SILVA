# DESAFIO SPRINT 5

### O objetivo do desafio da Sprint 5 é utilizar os conhecimentos adquiridos nos serviços AWS, principalmente no serviço S3. Um arquivo csv previamente baixado do site `dados.gov`, será enviado para um bucket S3 através de um script python, e uma vez lá, ele será analisado através de um segundo script python, de onde será produzido um outro arquivo csv com o resultado dessa análise. 

# Etapa 1: Preparação do ambiente conforme pedido no desafio

### Etapa 1.1: Logando no sistema da AWS através do sistema SSO onde localizei minhas credenciais

![Imagem ](/Sprint%205/EVIDENCIAS/EVIDENCIA_DESAFIO/img0.png)

### Etapa 1.2: Instalando o AWS CLI

![Imagem ](/Sprint%205/EVIDENCIAS/EVIDENCIA_DESAFIO/img1.png)

![Imagem ](/Sprint%205/EVIDENCIAS/EVIDENCIA_DESAFIO/img2.png)

### Etapa 1.2: Editei o arquivo credentials com minhas credenciais

![Imagem ](/Sprint%205/EVIDENCIAS/EVIDENCIA_DESAFIO/img3.png)

# Etapa 2: Obtendo a base de dados

### Etapa 2.1 : Entrei no site `dados.gov` escolhi a base de arrecadação por UF da Receita Federal, ela está explicada em detalhes no arquivo [BASE_DADOS](/Sprint%205/DESAFIO/BASE_DADOS.MD)

![Imagem ](/Sprint%205/EVIDENCIAS/EVIDENCIA_DESAFIO/img111.png)

# Etapa 3: Construção do código de envio do csv para o bucket S3 `envia.py`

### O código chamado envia.py realiza o upload de um arquivo para um bucket no Amazon S3.

### Ele faz as configurações de envio usando a biblioteca boto3 para criar uma sessão S3 para o perfil específico (AdministratorAccess-XXXXXXXXXX) e faz o upload do arquivo para o bucketandrebomfim.

### Antes de enviar, verifica se o arquivo existe localmente usando os.path.exists. Também faz uso de um bloco try-except para capturar e exibir mensagens de erro, me guiando caso algo saia errado.

![Imagem ](/Sprint%205/EVIDENCIAS/EVIDENCIA_DESAFIO/img22.png)

# Etapa 4: Construção do código de análise do csv no bucket S3 (`analise.py`)

### O código de analisa.py usa o pandas como principal ferramenta de manipulação de dados. Criei funções para baixar, enviar os dados, e a principal que irá analisar os dados. Nas funções de enviar e baixar os dados utilizo os recursos da boto3 para interagir com os recursos do S3. Como a interação com serviços cloud é um tanto "intangível", segui dicas de ............ para mostar se algum erro e qual estava ocorrendo.

### Na principal função do código, eu segui o passo a passo para verificação da correta análise da base de dados. Mostro as colunas disponíveis no dataframe,  mapeio elas, verifico as colunas realmente necessárias. Inicio o tratamento dos dados, como converter a coluna de imposto para tipo numérico e a remoção de valores inválidos (NaN) gerados por essa conversão que fiz.

### Esse código era obrigado a seguir itens descritos no texto do desafio, aliás, vou usar esse texto para comprovar que o que foi pedido foi seguido a risca.

![Imagem ](/Sprint%205/EVIDENCIAS/EVIDENCIA_DESAFIO/Etapa4/img1.png)

# Etapa 5: Envio para o bucket S3

### Para o envio dos arquivos, utilizei o mesmo bucket que criei para a relaização do exercício da seção 2.

### Saída do terminal do VS Code do após execução dos scripts envia.py e analisa.py

![Imagem](/Sprint%205/EVIDENCIAS/EVIDENCIA_DESAFIO/img34.png)

### Bucket S3 com os arquivos arrecadacao-estados.csv e resultado.csv

![Imagem](/Sprint%205/EVIDENCIAS/EVIDENCIA_DESAFIO/img35.png)

# Etapa 6: Entregas

### Nesta mostro a entrega dos scripts python produzidos e do arquivo trabalhado e o gerado.

[Script envia.py](/Sprint%205/DESAFIO/ARQUIVOS_DESAFIO/envia.py)

[Script analisa.py](/Sprint%205/DESAFIO/ARQUIVOS_DESAFIO/analisa.py)

[Arquivo csv arrecadacao-estado](/Sprint%205/DESAFIO/ARQUIVOS_DESAFIO/arrecadacao-estado.csv)

[Arquivo csv resultado.csv](/Sprint%205/DESAFIO/ARQUIVOS_DESAFIO/resultado.csv)

### Conforme exposto tudo exposto neste documento, considero entregue o desafio da Sprint 5.






