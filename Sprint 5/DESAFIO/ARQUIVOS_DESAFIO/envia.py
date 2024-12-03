import boto3
import os

def enviar_arquivo(bucket_name, file_name):
    try:
        s3 = session.client('s3')
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"Arquivo {file_name} enviado para o meu bucket {bucket_name}")
    except Exception as e:
        print(f"Erro ao enviar o arquivo: {e}")

if __name__ == "__main__":
    bucket_name = "bucketandrebomfim"
    file_name = "arrecadacao-estado.csv"

    if os.path.exists(file_name):
        enviar_arquivo(bucket_name, file_name)
    else:
        print(f"Arquivo {file_name} não encontrado.")
