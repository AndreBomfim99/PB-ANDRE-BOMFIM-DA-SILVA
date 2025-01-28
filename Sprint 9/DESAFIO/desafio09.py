import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, explode, from_json, current_date, year, month, dayofmonth
from pyspark.sql.types import ArrayType, StructType, StructField, StringType

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

TRUSTED_MOVIES_PATH = "s3://data-lake-andre-bomfim/Trusted/Parquet/Movies/"
TRUSTED_SERIES_PATH = "s3://data-lake-andre-bomfim/Trusted/Parquet/Series/"
TRUSTED_TMDB_PATH = "s3://data-lake-andre-bomfim/Trusted/Parquet/TMDB/processed_date=2025-01-27/"
REFINED_PATH = "s3://data-lake-andre-bomfim/Refined/Parquet/"

# Lê a Trusted Zone
movies_df = spark.read.parquet(TRUSTED_MOVIES_PATH) \
    .withColumnRenamed("notaMedia", "avaliacao_media") \
    .withColumnRenamed("numeroVotos", "quantidade_votos")

series_df = spark.read.parquet(TRUSTED_SERIES_PATH) \
    .withColumnRenamed("notaMedia", "avaliacao_media") \
    .withColumnRenamed("numeroVotos", "quantidade_votos")

tmdb_df = spark.read.parquet(TRUSTED_TMDB_PATH)

# Exibindo verific as colunas antes do processar
print("verif colunas emm movies_df:", movies_df.columns)
print("verif colunas em series_df:", series_df.columns)
print("verif colunas em tmdb_df:", tmdb_df.columns)

# desafio pede, confirmado 
tmdb_df = tmdb_df.withColumn("processed_date", current_date())

# Definindo schema para a genres
genres_schema = ArrayType(StructType([
    StructField("id", StringType(), True),
    StructField("name", StringType(), True)
]))

# Converte coluna genres de string p/ array 
tmdb_df = tmdb_df.withColumn("genres_array", from_json(col("genres"), genres_schema))

# Cria a dim_generos
dim_genero = tmdb_df.select(explode(col("genres_array")).alias("genero")) \
    .select(col("genero.id").alias("id_genero"), col("genero.name").alias("nome_genero")) \
    .distinct()

# Cria a dim_datas
dim_data = tmdb_df.select(col("processed_date")) \
    .withColumn("id_data", col("processed_date")) \
    .withColumn("ano", year(col("processed_date"))) \
    .withColumn("mes", month(col("processed_date"))) \
    .withColumn("dia", dayofmonth(col("processed_date"))) \
    .distinct()

# Cria a tabela fato_conteudo
fato_conteudo = movies_df.unionByName(series_df, allowMissingColumns=True) \
    .join(tmdb_df, movies_df["id"] == tmdb_df["id_tmdb"], "left") \
    .select(
        col("id").alias("id_conteudo"),
        tmdb_df["processed_date"].alias("id_data"),  # confirmar monitor esse detalhe
        col("avaliacao_media"),
        col("quantidade_votos"),
        col("popularity"),
        col("vote_average").alias("avaliacao_tmdb"),
        col("popularity").alias("popularidade_tmdb")
    )

# Faz o meio de campo do join com dim_genero 
fato_conteudo = fato_conteudo.join(dim_genero, fato_conteudo["id_conteudo"] == dim_genero["id_genero"], "left") \
    .select(
        col("id_conteudo"),
        col("id_genero"),  
        col("id_data"),
        col("avaliacao_media"),
        col("quantidade_votos"),
        col("popularity"),
        col("avaliacao_tmdb"),
        col("popularidade_tmdb")
    )

# conferir essa parte no cloudwatch - outputs - logs, tem que aparecer a qtdd 
print("Qtdd dimensao generos")
dim_genero.show(5)
print("Qtdd dimensão data")
dim_data.show(5)
print("Qtdd Tab Fato_Conteudo")
fato_conteudo.show(5)

# Salva os df na Refined Zone
dim_genero.write.parquet(f"{REFINED_PATH}/Dimensoes/Genero/", mode="overwrite")
dim_data.write.parquet(f"{REFINED_PATH}/Dimensoes/Data/", mode="overwrite")
fato_conteudo.write.parquet(f"{REFINED_PATH}/Fato/Conteudo/", mode="overwrite")

print("TABELAS OK E GRAVADAS NA REFINED ZONE")
job.commit()
