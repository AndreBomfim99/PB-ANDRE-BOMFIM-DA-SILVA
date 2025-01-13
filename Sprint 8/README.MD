# SPRINT 8

Nesta oitava sprint, assisti um curso rápido de AWS Analytics pelo Youtube. Também executei quatro exercícios, sendo os seguintes: 

- Três exercícios de geração de dados aleatórios:
1.  sendo um onde o código tem que gerar 20 nomes de animais ordenados de forma crescente e e imprimindo um a um em cada linha em um arquivo .csv, um segundo exercício onde tem que gerar 250 números inteiros e aleatórios. E um terceiro exercício onde gerei um dataset de nomes aleatórios de pessoas. Nele, importei as bibliotecas random, time e defini os parâmetros para geração do dataset como as quantidades de nomes aleatórios e a quantidade de nomes que devem ser únicos e e a semente de aleatoriedade.

- Um exercício de Apache Spark, onde usei o arquivo de nomes aleatórios gerado no terceiro exercício descrito acima, para criar um dataframe e testar comandos SQL. Iremos utilizar o arquivo nomes_aleatorios txt gerado na tarefa anterior. Adicionei colunas (Escolaridade, País e Ano de Nascimento) sem iteradores. O código ainda executa renomeamento de colunas, exibe esquemas, filtra dados por gerações e aplicar consultas com Spark SQL, com o objetivo de organizar dados por critérios de geração e país.

# 1. Exercícios:

## Exercío 1: Geração de 20 nomes de animais

#### Neste exercício declarei e inicializei uma lista que possui 20 nomes diferentes de animais. Ordenei esses nomes em ordem crescente e iterei sobre os mesmo, imprimindo um a um e armazenando o conteúdo da lista, um item em cada linha, no formato CSV.

[Código python](/Sprint%208/EXERCICIOS/EXE_GERACAO/gera20/gera20.py)

[Arquivo CSV](/Sprint%208/EXERCICIOS/EXE_GERACAO/gera20/animais.csv)

![imagem01](/Sprint%208/EVIDENCIAS/EXE_GERACAO/gera20/img01.png)

## Exercío 2: Geração de 250 números inteiros

#### Neste exercício, declarei e inicializei uma lista contendo 250 inteiros obtidos de forma aleatória. Em seguida apliquei o método reverse sobre o conteúdo da lista e mostro o resultado na saída.

[Código python](/Sprint%208/EXERCICIOS/EXE_GERACAO/gera250/gera250.py)

![imagem01](/Sprint%208/EVIDENCIAS/EXE_GERACAO/gera250/img01.png)

## Exercío 3: Geração de nomes

#### Neste exercício gerei um dataset de nomes aleatórios de pessoas. Nele, importei as bibliotecas random, time e defini os parâmetros para geração do dataset como as quantidades de nomes aleatórios e a quantidade de nomes que devem ser únicos e e a semente de aleatoriedade. O arquivo nomes_aleatorios.txt é muito grande, portanto, coloquei apenas um print do conteúdo deste.

[Código python](/Sprint%208/EXERCICIOS/EXE_GERACAO/geranomes/geranomes.py)

![imagem01](/Sprint%208/EVIDENCIAS/EXE_GERACAO/geranomes/img01.png)

![imagem02](/Sprint%208/EVIDENCIAS/EXE_GERACAO/geranomes/img02.png)

## Exercío 4: Dataframe com Apache Spark

#### Neste exercício, usei o arquivo de nomes aleatórios gerado no terceiro exercício descrito acima, para criar um dataframe e testar comandos SQL. Adicionei colunas (Escolaridade, País e Ano de Nascimento) sem iteradores. O código ainda executa renomeamento de colunas, exibe esquemas, filtra dados por gerações e aplicar consultas com Spark SQL, com o objetivo de organizar dados por critérios de geração e país.

[Código python](/Sprint%208/EXERCICIOS/EXE_SPARK/spark.py)

![imagem01](/Sprint%208/EVIDENCIAS/EXE_SPARK/img01.png)

![imagem02](/Sprint%208/EVIDENCIAS/EXE_SPARK/img02.png)

![imagem03](/Sprint%208/EVIDENCIAS/EXE_SPARK/img03.png)

![imagem04](/Sprint%208/EVIDENCIAS/EXE_SPARK/img04.png)

![imagem05](/Sprint%208/EVIDENCIAS/EXE_SPARK/img05.png)

![imagem06](/Sprint%208/EVIDENCIAS/EXE_SPARK/img06.png)

# 2. Evidências

###  Evidência da execução bem sucedida do Job 2 no Desafio 8

![imagem13](/Sprint%208/EVIDENCIAS/DESAFIO8/img13.png)

# 3. Certificados

### Nesta sprint não foram realizados cursos da AWS



