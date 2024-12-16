# SPRINT 6

Nesta sexta sprint 6 fiz 9 cursos sobre AWS no skillbuilder, esses cursos serão descritos logo abaixo na seção `3. Certificados`

Realizei ainda dois exercícios: 

- Um sobre `Athena`, onde configurei o AWS Athena e criei um ambiente de análise de dados baseado em um arquivo CSV armazenado no Amazon S3. 

- Outro sobre `Lambda`, onde criei uma função AWS Lambda para processar um arquivo no Amazon S3 usando Pandas.

Como desafio, criei um processo de ingestão batch em Python usando boto3, onde carrego arquivos CSV da minha máquina para um bucket S3 seguindo o padrão pedido no enunciado do desafio. A execução ocorre dentro de um container que está configurado com um volume para armazenar os arquivos e rodar o processo pela minha máquina local.

# 1. Exercícios:

### 1.1 Exercício sobre Athena

#### Neste exercício configurei o `Athena` para criar um ambiente de análise de dados para o arquivo CSV armazenado no meu bucket S3. Inicialmente preparei o bucket S3 com a criação de uma pasta QUERIES para armazenar os resultados das minhas consultas no Athena. Configurei o Athena Query Editor para direcionar os resultados das consultas para esse meu bucket. Usei o editor de consultas do Athena para criar um banco de dados com o comando `CREATE DATABASE` e defini uma tabela externa `CREATE EXTERNAL TABLE` com base nos dados que armazenei no S3. Executei as consultas SQL para validar a importação e analisei os dados no Athena, incluindo a criação de uma query que lista os 3 nomes mais usados em cada década. 

### Etapa 1: Aproveitei o bucket criado em sprint anterior e criei a pasta `QUERIES`

![imagem01](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Athena/img01.png)

### Etapa 2: No query editor do Athena criei o banco `meubanco`

![imagem02](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Athena/img02.png)

### Etapa 3: No query editor do Athena criei também a tabela `minhatabela`

![imagem03](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Athena/img03.png)

### Etapa 4: Criei a query que lista os 3 nomes mais usados em cada década.  

![imagem04](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Athena/img04.png)

### Etapa 5: Saída da consulta

![imagem05](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Athena/img05.png)

### Etapa 6: Saída na pasta QUERIES

![imagem06](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Athena/img06.png)

### Etapa 7: Endpoint do object CSV gerado na consulta 

![imagem07](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Athena/img07.png)

### Etapa 8: O arquivo CSV gerado, aberto no librecalc 

![imagem08](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Athena/img08.png)


### 1.2 Exercício sobre Lambda

#### Neste exercício sobre Lambda criei uma função `Lambda` para processar o arquivo que está no bucket S3 usando `Pandas`. Na função Lambda configurei ela com python 3.9, e código do script consegue ler o arquivo CSV no S3 e retorna o número de linhas. Como o ambiente do Lambda não tem Pandas, criei uma Layer personalizada com essa dependência usando Docker, compactei em um arquivo zip e carreguei no Lambda. Usei a layer anexada à função Lambda, permitindo que eu use Pandas normalmente. Ainda fiz a configuração das permissões adicionando uma política do IAM para garantir que o Lambda acesse o meu bucket S3.

### Etapa 1: Criando a função Lambda no AWS

![imagem01](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img01.png)

### Etapa 2: Código da minha função Lambda

![imagem02](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img02.png)

### Etapa 3: Erro esperado pois a função ainda não tem a biblioteca Pandas implementada

![imagem03](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img03.png)

### Etapa 4: Criação do container Docker com a imagem Linux

![imagem05](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img05.png)

### Etapa 5: Fazendo o build do container 

![imagem06](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img06.png)

### Etapa 6: Criação dos diretórios dentro do container

![imagem07](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img07.png)

### Etapa 7: Instalação do Pandas

![imagem07](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img07a.png)

### Etapa 8: Compactando todos os arquivos em um arquivo chamado minha-camada-pandas.zip.

![imagem08](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img08.png)

### Etapa 9: Carregando o minha-camada-pandas.zip para o bucket

![imagem09](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img09.png)

### Etapa 10: Criando a Layer apontando para o minha-camada-pandas.zip

![imagem10](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img10.png)

### Etapa 11: Executando novamente o código na função Lambda e obtendo o resultado esperado

![imagem11](/Sprint%206/EVIDENCIAS/EVIDENCIA_EXERCICIO/exe_Lambda/img11.png)


# 2. Evidências



# 3. Certificados

#### Foram realizados 9 cursos sobre AWS no skillbuilder: Fundamentals of Analytics on AWS – Part 1 e Part 2, Serverless Analytics, Introduction to Amazon Athena, Glue Getting Started, EMR Getting Started, Getting Started with Amazon Redshift, Best Practices for Data Warehousing with Amazon Redshift, Amazon QuickSight.

### Comprovante de conclusão Fundamentals of Analytics on AWS – Part 1 

![Certificado](/Sprint%206/CERTIFICADOS/Fundamentals-of-Analytics-on-AWS-Part-1.jpg)

### Comprovante de conclusão Fundamentals of Analytics on AWS – Part 2

![Certificado](/Sprint%206/CERTIFICADOS/Fundamentals-of-Analytics-on-AWS-Part-2.jpg)

### Comprovante de conclusão Serverless Analytics 

![Certificado](/Sprint%206/CERTIFICADOS/Serverless-Analytics.jpg)

### Comprovante de conclusão Introduction to Amazon Athena

![Certificado](/Sprint%206/CERTIFICADOS/Introduction-to-Amazon-Athena.jpg)

### Comprovante de conclusão AWS Glue Getting Started 

![Certificado](/Sprint%206/CERTIFICADOS/AWS-Glue-Getting-Started.jpg)

### Comprovante de conclusão Amazon EMR Getting Started 

![Certificado](/Sprint%206/CERTIFICADOS/Amazon-EMR-Getting-Started.jpg)

### Comprovante de conclusão Getting Started with Amazon Redshift 

![Certificado](/Sprint%206/CERTIFICADOS/Getting-Started-with-Amazon-Redshift.jpg)

### Comprovante de conclusão Best Practices for Data Warehousing with Amazon Redshift

![Certificado](/Sprint%206/CERTIFICADOS/Best-Practices-for-Data-Warehousing-with-Amazon-Redshift.jpg)

### Comprovante de conclusão Amazon QuickSight 

![Certificado](/Sprint%206/CERTIFICADOS/Amazon-QuickSight.jpg)



