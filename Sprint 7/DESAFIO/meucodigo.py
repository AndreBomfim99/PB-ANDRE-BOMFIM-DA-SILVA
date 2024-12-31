import os
import boto3
import json
from datetime import datetime
from tmdbv3api import TMDb, Discover

tmdb = TMDb()

tmdb.language = 'pt-BR'  
tmdb.debug = True  

descobrir = Discover()

cliente_s3 = boto3.client('s3')

def manipulador_lambda(evento, contexto):
   
    bucket = 'data-lake-andre-bomfim'
    generos = {"Drama": 18, "Romance": 10749}  # 18 e 10749 são os IDs de gênero do TMDB
    anos = [2022, 2023]  

    for ano in anos:
        for genero, id_genero in generos.items():
            print(f"Iniciando a extração de dados para {genero} no ano de {ano}.")

            filmes = buscar_dados(descobrir, ano, id_genero, tipo_midia='movie')
            salvar_no_s3(filmes, bucket, ano, genero, 'filme')
            series = buscar_dados(descobrir, ano, id_genero, tipo_midia='tv')
            salvar_no_s3(series, bucket, ano, genero, 'serie')

def buscar_dados(api_descobrir, ano, id_genero, tipo_midia):
  
    print(f"Buscando dados para o gênero ID {id_genero} no ano {ano}. Tipo: {tipo_midia}.")
    resultados = []
    pagina = 1
    while True:
        print(f"Fazendo requisição para a página {pagina}.")
        try:
            if tipo_midia == 'movie':
                resposta = api_descobrir.discover_movies({
                    'with_genres': id_genero,
                    'primary_release_year': ano,
                    'page': pagina
                })
            elif tipo_midia == 'tv':
                resposta = api_descobrir.discover_tv_shows({
                    'with_genres': id_genero,
                    'first_air_date_year': ano,
                    'page': pagina
                })
            else:
                print(f"Tipo de mídia inválido: {tipo_midia}.")
                break
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
            break

        if not resposta:
            print("Nenhum dado encontrado ou fim das páginas.")
            break
        resultados.extend(resposta)
        pagina += 1
        if pagina > 5: 
            print("Limite de páginas atingido (5).")
            break
    print(f"Dados coletados: {len(resultados)} registros.")
    return resultados

def salvar_no_s3(dados, bucket, ano, genero, tipo_midia):
   
    if not dados:
        print("Nenhum dado para salvar no S3.")
        return

    print(f"Dividindo todos os dados em lotes de 100 registros.")
    lotes = [dados[i:i + 100] for i in range(0, len(dados), 100)]
    for indice, lote in enumerate(lotes):
        agora = datetime.utcnow()
        caminho_data = agora.strftime("%Y/%m/%d")
        nome_arquivo = f"{tipo_midia}-{genero}-{ano}-{indice + 1}-{agora.strftime('%H%M%S')}.json"
        caminho = f"Raw/TMDB/JSON/{caminho_data}/{nome_arquivo}"

        try:
            dados_json = json.dumps(lote, default=str)  

            # Enviar para o S3
            cliente_s3.put_object(
                Bucket=bucket,
                Key=caminho,
                Body=dados_json,
                ContentType='application/json'
            )
            print(f"Arquivo salvo: {caminho} com {len(lote)} registros.")
        except Exception as e:
            print(f"Erro ao salvar no S3: {e}")
