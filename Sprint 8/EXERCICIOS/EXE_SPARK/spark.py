import random
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, when, col, expr

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

caminho_arquivo = "C:/EXE_SPARK/nomes_aleatorios.txt"
dados = spark.read.csv(caminho_arquivo, header=True, inferSchema=True)
dados.show(5)
dados = dados.withColumnRenamed(dados.columns[0], "Nomes")
dados.printSchema()
dados.show(10)

escolaridade = ["Fundamental", "Medio", "Superior"]
dados = dados.withColumn(
    "Escolaridade",
    expr(f"array({','.join([f'\'{e}\'' for e in escolaridade])})[int(rand()*3)]")
)

paises = [
    "Brasil", "Argentina", "Chile", "Colômbia", "Uruguai", "Paraguai",
    "Bolívia", "Peru", "Equador", "Venezuela", "Guiana", "Suriname", "Guiana Francesa"
]
dados = dados.withColumn(
    "Pais",
    expr(f"array({','.join([f'\'{p}\'' for p in paises])})[int(rand()*13)]")
)

dados = dados.withColumn(
    "AnoNascimento",
    expr("1945 + int(rand()*66)")
)

dados.show(5)

pega_select = dados.filter(col("AnoNascimento") >= 2000)
pega_select.show(10)

dados.createOrReplaceTempView("pessoas")
select-sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")
select-sql.show(10)

df_millennials = dados.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994))
print(f"Millennials: {df_millennials.count()}")

qtdd-millen = spark.sql("SELECT COUNT(*) as total FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")
qtdd-millen.show()

dados = dados.withColumn(
    "Geracao",
    when(col("AnoNascimento").between(1944, 1964), "Baby Boomers")
    .when(col("AnoNascimento").between(1965, 1979), "Geração X")
    .when(col("AnoNascimento").between(1980, 1994), "Millennials")
    .when(col("AnoNascimento").between(1995, 2015), "Geração Z")
)

df_geracoes = dados.groupBy("Pais", "Geracao").count().orderBy("Pais", "Geracao")
df_geracoes.show()

spark.stop()
