import requests
import pandas as pd

genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"

# Obter os IDs dos gêneros Drama e Romance
response = requests.get(genre_url)
genres_data = response.json()

genre_ids = []
for genre in genres_data['genres']:
    if genre['name'].lower() in ['drama', 'romance']:
        genre_ids.append(genre['id'])

if not genre_ids:
    raise ValueError("Aviso: Nao e possível encontrar filmes de Drama e Romance")

# Consultar filmes filtrando pelos gêneros Drama e Romance
url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&with_genres={','.join(map(str, genre_ids))}"
response = requests.get(url)
data = response.json()

# Verificar os dados retornados
print("Dados da API:")
print(data)

filmes = []
for movie in data.get('results', []):
    df = {
        'Titulo': movie['title'],
        'Data de lancamento': movie['release_date'],
        'Visao geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Media de votos': movie['vote_average']
    }
    filmes.append(df)

# Criar DataFrame
df = pd.DataFrame(filmes)

# Verificar se há dados antes de salvar
if not df.empty:
    df.to_csv('filmes_drama_romance.csv', index=False, encoding='utf-8-sig')
    print("Arquivo 'filmes_drama_romance.csv' gerado")
else:
    print("Nenhum filme encontrado de Drama/Romance.")
