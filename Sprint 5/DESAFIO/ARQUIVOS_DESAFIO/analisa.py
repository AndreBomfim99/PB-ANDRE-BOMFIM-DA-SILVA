import boto3
import pandas as pd
import os

def baixar_csv(bucket_name, file_name, download_path):
    s3 = session.client('s3')
    try:
        s3.download_file(bucket_name, file_name, download_path)
        print(f"O csv {file_name} foi baixado.")
    except Exception as e:
        print(f"Deu erro ao baixar o csv: {e}")
        raise

def enviar_csv(bucket_name, file_name, upload_path):
    session = boto3.Session(profile_name="AdministratorAccess-908027386897")
    s3 = session.client('s3')
    try:
        s3.upload_file(upload_path, bucket_name, file_name)
        print(f"Arquivo {file_name} enviado para o bucket {bucket_name}")
    except Exception as e:
        print(f"Erro ao enviar meu arquivo {e}")
        raise

def analisar_dados(file_path):
    df = pd.read_csv(file_path)

    print("Colunas disponíveis:", df.columns)

    coluna_estado = 'UF'
    coluna_imposto = 'IMPOSTO SOBRE IMPORTACAO' 

    if coluna_estado not in df.columns or coluna_imposto not in df.columns:
        raise ValueError(f"Colunas '{coluna_estado}' ou '{coluna_imposto}' estão ausentes no arquivo CSV.")
    
    df[coluna_imposto] = pd.to_numeric(df[coluna_imposto], errors='coerce')
    df = df.dropna(subset=[coluna_imposto])

    ############## Aqui começam os itens pedidos no Desafio 5 ######################

    # 4.1. Um Cláusula que filtra dados usando ao menos dois operadores lógicos
    filtro = df[(df[coluna_imposto] > 10000) & (df[coluna_estado] != 'SP')]

    # 4.2. Duas funções de Agregação
    agregacao = filtro.groupby(coluna_estado).agg({'IMPOSTO SOBRE IMPORTACAO': ['sum', 'mean']})

    # 4.3. Uma função Condicional
    df['categoria'] = df['IMPOSTO SOBRE IMPORTACAO'].apply(lambda x: 'Alta' if x > 50000 else 'Baixa')

    # 4.4. Uma função de Conversão
    df['arrecadacao_milhoes'] = df['IMPOSTO SOBRE IMPORTACAO'] / 1e6

    # 4.5. Uma função de Data
    if 'ANO' in df.columns:
        df['ano'] = df['ANO']

    # 4.6. Uma função de String
    df['estado_maiusculo'] = df[coluna_estado].str.upper()

    # Cálculos solicitados
    total_arrecadacao = df['IMPOSTO SOBRE IMPORTACAO'].sum()

    ranking = df.groupby(coluna_estado)['IMPOSTO SOBRE IMPORTACAO'].sum().sort_values(ascending=False)

    df['percentual'] = (df['IMPOSTO SOBRE IMPORTACAO'] / total_arrecadacao) * 100

    resultado = pd.DataFrame({
        'Estado': ranking.index,
        'Arrecadação Total': ranking.values,
        'Percentual': [round(x, 2) for x in (ranking / total_arrecadacao) * 100]
    })

    resultado.to_csv('resultado.csv', index=False)
    print("Arquivo resultado.csv criado.")

if __name__ == "__main__":
    bucket_name = "bucketandrebomfim"
    file_name = "arrecadacao-estado.csv"
    download_path = file_name
    upload_path = "resultado.csv"

    baixar_csv(bucket_name, file_name, download_path)
    analisar_dados(download_path)
    enviar_csv(bucket_name, upload_path, upload_path)
