#JOB 2 PROCESSA TMDB

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

RAW_TMDB_PATH = "s3://data-lake-andre-bomfim/Raw/TMDB/JSON/2025/01/13/"
TRUSTED_PATH = "s3://data-lake-andre-bomfim/Trusted/Parquet/TMDB"

dataframetmdb = spark.read.json(RAW_TMDB_PATH)

print("ATENÇÃO: JSON FOI LIDO CORRETAMENTE")
dataframetmdb.show(5)
dataframetmdb.printSchema()

# ConverTE tipos e faz limpeza
dataframetmdb = dataframetmdb.withColumn("anoLancamento", col("release_date").substr(1, 4).cast(IntegerType()))
dataframetmdb = dataframetmdb.withColumn("popularity", col("popularity").cast("double"))
dataframetmdb = dataframetmdb.withColumn("vote_average", col("vote_average").cast("double"))
dataframetmdb = clean_data(dataframetmdb).filter(
    (col("anoLancamento") >= 2010) & (col("anoLancamento") <= 2023)
)

dataframetmdb = dataframetmdb.withColumn("processed_date", current_date())
dataframetmdb.write.mode("overwrite").partitionBy("processed_date").parquet(TRUSTED_PATH)
print("Processamento do Job 2 concluído. Dados salvos no S3.")
job.commit()
