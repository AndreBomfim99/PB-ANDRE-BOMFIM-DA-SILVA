import os
import boto3
import json
from datetime import datetime
from tmdbv3api import TMDb, Discover

tmdb = TMDb()

tmdb.language = 'pt-BR'  
tmdb.debug = True  

discover = Discover()

s3_client = boto3.client('s3')

def lambda_handler(event, context):
   
    bucket = 'data-lake-andre-bomfim'
    genres = {"Drama": 18, "Romance": 10749}  # 18 e 10749 são os IDs de gênero do TMDB
    years = [2022, 2023]  

    for year in years:
        for genre, genre_id in genres.items():
            print(f"Iniciando a extração de dados para {genre} no ano de {year}.")

            movies = fetch_data(discover, year, genre_id, media_type='movie')
            save_to_s3(movies, bucket, year, genre, 'movie')
            series = fetch_data(discover, year, genre_id, media_type='tv')
            save_to_s3(series, bucket, year, genre, 'series')

def fetch_data(discover_api, year, genre_id, media_type):
    print(f"Buscando dados para o gênero ID {genre_id} no ano {year}. Tipo: {media_type}.")
    results = []
    page = 1
    while True:
        print(f"Fazendo requisição para a página {page}.")
        try:
            if media_type == 'movie':
                response = discover_api.discover_movies({
                    'with_genres': genre_id,
                    'primary_release_year': year,
                    'page': page
                })
            elif media_type == 'tv':
                response = discover_api.discover_tv_shows({
                    'with_genres': genre_id,
                    'first_air_date_year': year,
                    'page': page
                })
            else:
                print(f"Tipo de mídia inválido: {media_type}.")
                break
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
            break

        if not response:
            print("Nenhum dado encontrado ou fim das páginas.")
            break
        results.extend(response)
        page += 1
        if page > 5: 
            print("Limite de páginas atingido (5).")
            break
    print(f"Dados coletados: {len(results)} registros.")
    return results

def save_to_s3(data, bucket, year, genre, media_type):
    """
    Salva os dados em lotes no bucket S3.
    """
    if not data:
        print("Nenhum dado para salvar no S3.")
        return

    print(f"Dividindo todos os dados em lotes de 100 registros.")
    chunks = [data[i:i + 100] for i in range(0, len(data), 100)]
    for idx, chunk in enumerate(chunks):
        now = datetime.utcnow()
        date_path = now.strftime("%Y/%m/%d")
        file_name = f"{media_type}-{genre}-{year}-{idx + 1}-{now.strftime('%H%M%S')}.json"
        path = f"Raw/TMDB/JSON/{date_path}/{file_name}"

        try:
            json_data = json.dumps(chunk, default=str)  

            # Enviar para o S3
            s3_client.put_object(
                Bucket=bucket,
                Key=path,
                Body=json_data,
                ContentType='application/json'
            )
            print(f"Arquivo salvo: {path} com {len(chunk)} registros.")
        except Exception as e:
            print(f"Erro ao salvar no S3: {e}")
