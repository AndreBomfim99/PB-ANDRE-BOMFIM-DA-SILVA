# JOB 1 PROCESSA CSV

import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, current_date
from pyspark.sql.types import IntegerType

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

def clean_data(df):
    return df.replace(["\\n", ""], None).dropna(how="any")

RAW_MOVIES_PATH = "s3://data-lake-andre-bomfim/Raw/Local/CSV/Movies/2024/12/13/movies.csv"
RAW_SERIES_PATH = "s3://data-lake-andre-bomfim/Raw/Local/CSV/Series/2024/12/13/series.csv"
TRUSTED_PATH = "s3://data-lake-andre-bomfim/Trusted/Parquet"

###########################################################################################
# Este trecho lida com o separador "|" 

movies_df = spark.read.csv(RAW_MOVIES_PATH, header=True, inferSchema=True, sep="|")
series_df = spark.read.csv(RAW_SERIES_PATH, header=True, inferSchema=True, sep="|")

###########################################################################################

print("ATENÇÃO: MOVIES.CSV E SERIES.CSV FORAM LIDOS")
movies_df.show(5)
series_df.show(5)


########################################################################################################
# Limpeza e conversão de tipo, primeiro para filmes e depois series
movies_df = movies_df.withColumn("anoLancamento", col("anoLancamento").cast(IntegerType()))
movies_df = movies_df.withColumn("tempoMinutos", col("tempoMinutos").cast(IntegerType()))
movies_df = movies_df.withColumn("numeroVotos", col("numeroVotos").cast(IntegerType()))
movies_df = movies_df.withColumn("notaMedia", col("notaMedia").cast("double"))
movies_df = clean_data(movies_df).filter(
    (col("anoLancamento") >= 2010) & (col("anoLancamento") <= 2023)
)
series_df = series_df.withColumn("anoLancamento", col("anoLancamento").cast(IntegerType()))
series_df = series_df.withColumn("tempoMinutos", col("tempoMinutos").cast(IntegerType()))
series_df = series_df.withColumn("numeroVotos", col("numeroVotos").cast(IntegerType()))
series_df = series_df.withColumn("notaMedia", col("notaMedia").cast("double"))
series_df = clean_data(series_df).filter(
    (col("anoLancamento") >= 2010) & (col("anoLancamento") <= 2023)
)
##########################################################################################################

movies_df = movies_df.withColumn("processed_date", current_date())
series_df = series_df.withColumn("processed_date", current_date())
movies_df.write.mode("overwrite").parquet(f"{TRUSTED_PATH}/Movies")
series_df.write.mode("overwrite").parquet(f"{TRUSTED_PATH}/Series")
print("ATENÇÃO: OS DADOS FORAM SALVS NO S3")
job.commit()
