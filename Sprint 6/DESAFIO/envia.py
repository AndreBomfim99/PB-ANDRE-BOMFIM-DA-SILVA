import boto3
import os
import csv
from datetime import datetime
from botocore.exceptions import ClientError

def carregar_credenciais():
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_session_token = os.getenv('AWS_SESSION_TOKEN')
    aws_region = os.getenv('AWS_REGION')

    if not all([aws_access_key_id, aws_secret_access_key, aws_session_token]):
        raise EnvironmentError("AVISO: MINHAS CREDENCIAIS NAO FORAM ENCONTRADAS NAS VARIAVEIS DE AMBIENTE")
    if not aws_region:
        raise EnvironmentError("AVISO: A REGIAO AWS NÃO FOI ENCONTRADA NAS VARIAVEIS DE AMBIENTE")

    return aws_access_key_id, aws_secret_access_key, aws_session_token, aws_region

def criar_bucket(s3_client, bucket_name, region):
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"AVISO: O '{bucket_name}' JA EXISTE NO S3.")
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"AVISO: MEU BUCKET '{bucket_name}' NAO ESTA NO S3. O SCRIPT VAI CRIAR")
            try:
                if region == region:
                    s3_client.create_bucket(Bucket=bucket_name)
                else:
                    s3_client.create_bucket(
                        Bucket=bucket_name,
                        CreateBucketConfiguration={'LocationConstraint': region}
                    )
                print(f"AVISO: BUCKET '{bucket_name}' CRIADO COM SUC")
            except ClientError as e:
                print(f"AVISO: ERRO AO CRIAR {e}")
                raise
        else:
            raise

def carregar_para_s3(s3_client, bucket, camada, origem, formato, especificacao, arquivo_csv, nome_arquivo):
    data_atual = datetime.now()
    caminho_s3 = f"{camada}/{origem}/{formato}/{especificacao}/{data_atual.year}/{data_atual.month:02}/{data_atual.day:02}/{nome_arquivo}"
    try:
        s3_client.upload_file(arquivo_csv, bucket, caminho_s3)
        print(f"AVISO: ARQUIVO {nome_arquivo} ENVIADO PARA {caminho_s3}")
    except ClientError as e:
        print(f"AVISO: ERRO AO ENVIAR {nome_arquivo} PARA O S3: {e}")
        raise

movies_csv = 'movies.csv'
series_csv = 'series.csv'
bucket_name = 'data-lake-andre-bomfim'

aws_access_key_id, aws_secret_access_key, aws_session_token, aws_region = carregar_credenciais()

s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=aws_region
)

criar_bucket(s3_client, bucket_name, region=aws_region)

for arquivo in [movies_csv, series_csv]:
    if not os.path.exists(arquivo):
        raise FileNotFoundError(f"AVISO: O ARQUIVO {arquivo} NÃO FOI ENCONTRADO NO VOLUME")

for arquivo, nome in [(movies_csv, 'movies.csv'), (series_csv, 'series.csv')]:
    carregar_para_s3(s3_client, bucket_name, 'Raw', 'Local', 'CSV', nome.split('.')[0].capitalize(), arquivo, nome)
