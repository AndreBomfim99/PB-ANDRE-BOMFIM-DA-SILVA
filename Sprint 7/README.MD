# SPRINT 7

Nesta sétima sprint, tomei conhecimento do que é e para que serve o Apache Spark através de um curso da Udemy. Esse curso e a ferramenta Spark me ajudaram a entender melhor conceitos de ciências de dados e como ter uma melhor produtividade. Ainda realizei 3 exercícios.  

O primeiro exercício era um ETL no serviço AWS Glue, onde preparei dados, configurei um role no IAM e um crawler no Lake Formation. Ainda escrevi um código que realiza uma tarefa pedida no exercício.

O segundo exercício é a implementação dos conhecimentos adquiridos no curso de Spark, onde implementei um código que faz processamento através de Docker e conta palavras de um Readme.

O terceiro exercício criei um processo de extração de dados utilizando a API do TMDB com a ajuda de serviços da AWS.

Por fim, o desafio é realizar a ingestão de API, onde capturei dados do TMDB usando o serviço AWs Lambda, onde ele faz chamadas da API. Esse desafio é referente a etapa 2 do desafio principal que foi iniciado na sprint anterior.


# 1. Exercícios:

### 1.1 Exercício Glue: Neste exercício elaborei um processo de ETL, onde usei serviços do Glue e do Lake Formation

![imagem02](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img02.png)

![imagem03](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img03.png)

![imagem04](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img04.png)

![imagem05](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img05.png)

![imagem06](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img06.png)

![imagem07](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img07.png)

![imagem08](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img08.png)

![imagem09](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img09.png)

![imagem10](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img10.png)

![imagem11](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img11.png)

![imagem12](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img12.png)

![imagem13](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img13.png)

![imagem14](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img14.png)

![imagem15](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img15.png)

![imagem16](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img16.png)

![imagem17](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img17.png)

![imagem18](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img18.png)

![imagem19](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img19.png)

![imagem20](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img20.png)

![imagem21](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img21.png)

![imagem22](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img22.png)

![imagem23](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img23.png)

![imagem24](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img24.png)

![imagem25](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img25.png)

![imagem26](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img26.png)

![imagem27](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img27.png)

![imagem28](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img28.png)

![imagem29](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img29.png)

![imagem30](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img30.png)

![imagem31](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img31.png)

![imagem32](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img32.png)

![imagem33](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img33.png)

![imagem34](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img34.png)

![imagem35](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img35.png)

![imagem36](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img36.png)

![imagem37](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img37.png)

![imagem38](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img38.png)

![imagem39](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img39.png)

![imagem40](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img40.png)

![imagem41](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img41.png)

![imagem42](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img42.png)

![imagem43](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img43.png)

![imagem45](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img45.png)

![imagem46](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img46.png)

![imagem47](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img47.png)

![imagem48](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img48.png)

![imagem49](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img49.png)

![imagem50](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img50.png)

![imagem51](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img51.png)

![imagem52](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_GLUE/img52.png)

### Resultado do exercício de Glue

Arquivo CSV [resultado.csv](/Sprint%207/EXERCICIOS/EXE_GLUE/resultado.csv)

### 1.2 Exercício sobre Apache Spark: Neste exercício implementei um código que faz processamento através de Docker e conta palavras de um Readme.

![imagem01](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img01.png)

![imagem02](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img02.png)

![imagem03](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img03.png)

![imagem04](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img04.png)

![imagem05](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img05.png)

![imagem06](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img06.png)

![imagem07](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img07.png)

![imagem08](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img08.png)

![imagem09](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img09.png)

### Obs.: O arquivo que eu usei para ter suas palavras contadas foi o README de apresentação. 

![imagem10](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img10.png)

![imagem11](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img11.png)

![imagem12](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img12.png)

![imagem13](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img13.png)

![imagem14](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_SPARK/img14.png)

### Arquivos gerados no exercício de Spark

Código em Jupyter (Google Colab) [exe_spark.ipynb](/Sprint%207/EXERCICIOS/EXE_SPARK_COLAB/exe_spark.ipynb)

Código em Python [exe_spark.py](/Sprint%207/EXERCICIOS/EXE_SPARK_COLAB/exe_spark.py)

Resultado em CSV [quantidade_palavras.csv](/Sprint%207/EXERCICIOS/EXE_SPARK_COLAB/quantidade_palavras.csv)


### 1.3 Exercício sobre a API TMDB: Neste exercício criei um processo de extração de dados da API da TMDB

### 1.3.1:  Criei minha conta no TMDB

![imagem01](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_TMDB/img01.png)

![imagem02](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_TMDB/img02.png)

![imagem03](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_TMDB/img03.png)

### 1.3.4:  Executei o script a partir de um container Docker

![imagem04](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_TMDB/img04.png)

### 1.3.5:  Uma parte do meu script para acessar o TMDB

![imagem05](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_TMDB/img05.png)

### 1.3.6:  O resultado da consulta gravei em um arquivo .CSV

![imagem06](/Sprint%207/EVIDENCIAS/EVIDENCIAS_EXE_TMDB/img06.png)

### 1.3.7: Arquivos gerados do exercício do TMDB

Arquivo [Dockerfile](/Sprint%207/EXERCICIOS/EXE_TMDB/Dockerfile)

Script [dramaromance.py](/Sprint%207/EXERCICIOS/EXE_TMDB/dramaromance.py)

Arquivo CSV [filmes_drama_romance.csv](/Sprint%207/EXERCICIOS/EXE_TMDB/filmes_drama_romance.csv)

# 2. Evidências

### Print do resultado final do Desafio

![imagem26](/Sprint%207/EVIDENCIAS/EVIDENCIAS_DESAFIO/img26.png)

# 3. Certificados

### Nesta sprint não foram realizados cursos da AWS



