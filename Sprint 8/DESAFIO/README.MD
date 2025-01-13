# DESAFIO SPRINT 8

### O objetivo do desafio da Sprint 8 consiste em processar os dados da Raw Zone para uma camada Trusted do meu datalake, que se localiza no meu bucket S3 utilizando Apache Spark no AWS Glue. Os dados serão padronizados no formato PARQUET, particionados por data de criação e armazenados no S3 para análise via AWS Athena. O processamento será dividido em dois "jobs" do Spark no Aws Glue, sendo  um para arquivos CSV e outro para dados da API TMDB. Esses jobs devem ser criados no Spark script editor. 

### Tendo os códigos dos job 1 (para os arquivos CSV) e job 2 (para a API TMDB), o processo de implementação no AWS Glue envolve apenas configuração e execução.

### Sobre minhas perguntas que serão objetos de análise: O cerne da minha análise consistia em comparar performances entre séries e filmes para obter um meio de saber, a depender da história e conteúdo, onde seria mais rentável investir, em um filme ou em uma série. Mas, apesar de ser possível realizar, ela se revelou uma análise trabalhosa demais, implicando em custos financeiros que vão além do que o PB UOL permite. Então decidi dar um passo atrás e simplificar a análise, mantendo pelo menos algo que pudesse abarcar uma análise sobre séries. Aqui estão: 

### Perguntas sobre Filmes

### Análise de Gêneros Drama e Romance

- Qual é o tempo médio de duração de filmes de Drama e Romance?
- Filmes de Drama ou Romance têm maior aceitação em termos de avaliação média e número de votos?
- Quais são os filmes de Drama ou Romance mais votados? 
- Qual gênero (Drama ou Romance) tem maior popularidade média em filmes?
- Quais anos tiveram mais lançamentos de filmes de Drama ou Romance?

### Análise Financeira
- Quais filmes de Drama ou Romance têm as maiores receitas em relação ao orçamento?
- Filmes de Drama ou Romance com maior avaliação tendem a ter maior receita?
- Quais são os anos mais lucrativos para filmes de Drama ou Romance?

### Análise de Produtoras, Países e Elencos
- Quais produtoras produzem mais filmes de Drama ou Romance?
- Quais países produzem mais filmes de Drama ou Romance? 
- Quais são os diretores mais frequentes em filmes de Drama ou Romance? 
- Quais atores ou atrizes aparecem com mais frequência em filmes de Drama ou Romance?

### Perguntas sobre Filmes que Viraram Séries
- Quais séries, spinoffs ou derivadas surgiram de filmes?
- Quais atores ou atrizes dos filmes participaram das séries derivadas?

## Início do Desafio Sprint 8

### Etapa 1: Nesta etapa acesso o AWS Glue para criar o job 1, onde vou processar os dados dos arquivos CSV

![imagem03](/Sprint%208/EVIDENCIAS/DESAFIO8/img03.png)

### Etapa 2: Acessando o AWS Glue Studio para criar o job 1

![imagem04](/Sprint%208/EVIDENCIAS/DESAFIO8/img04.png)

### Etapa 3: Criei o job 1 como `proce_csv_p_trusted`e fiz as configurações conforme pedido no Desafio 8. Aproveitei o IAM Role AWSGlueServiceRole-Lab4 do exercício da Sprint 7.

![imagem05](/Sprint%208/EVIDENCIAS/DESAFIO8/img05.png)

### Etapa 4: Continuação das configurações, sendo as principais o Spark como Tipo do job, Python 3 para codificação e o worker como G 1X

![imagem06](/Sprint%208/EVIDENCIAS/DESAFIO8/img06.png)

### Etapa 5: Mesmo processo foi usado para criar o job 2 `processa_tmdb_p_trusted`

![imagem07](/Sprint%208/EVIDENCIAS/DESAFIO8/img07.png)

### Etapa 6: Job 1 e Job 2 criados, vou agora inserir os script que já foram previamente escritos e testados

![imagem09](/Sprint%208/EVIDENCIAS/DESAFIO8/img09.png)

### Etapa7: Script do job 1, ele vai processar e enviar os dados dos csvs `movies.csv`e `series.csv`que estão no meu bucket (camada Raw) e enviá-los para a camada Trusted.

![imagem10](/Sprint%208/EVIDENCIAS/DESAFIO8/img10.png)

### Etapa 8: Evidência da execução bem sucedida do Job 1.

![imagem11](/Sprint%208/EVIDENCIAS/DESAFIO8/img11.png)

## Etapa 9: Script do job 2, ele vai processar e enviar os dados coletados da `API TMDB`e que estão no meu bucket (camada Raw) e enviá-los para a camada Trusted.

![imagem12](/Sprint%208/EVIDENCIAS/DESAFIO8/img12.png)

### Etapa 10:  Evidência da execução bem sucedida do Job 2, sendo que foram 2 execuções que falharam anteriormente devido a falta de configuração das políticas de acesso.

![imagem13](/Sprint%208/EVIDENCIAS/DESAFIO8/img13.png)

### Etapa 11: Evidência do buckets criados 

![imagem14](/Sprint%208/EVIDENCIAS/DESAFIO8/img14.png)

### Etapa 12: Evidência dos arquivos parquet criados dentro de Movies

![imagem15](/Sprint%208/EVIDENCIAS/DESAFIO8/img15.png)

#### Diante de tudo exposto no presente documento, dou por entregue e finalizado o desafio da Sprint 8.