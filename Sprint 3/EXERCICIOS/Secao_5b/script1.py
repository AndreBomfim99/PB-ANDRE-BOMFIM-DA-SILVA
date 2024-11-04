# Caminho do arquivo
caminho_arquivo = 'actors.csv'
# Caminhos para os arquivos de saída
caminho_etapa_1 = 'etapa-1.txt'
caminho_etapa_2 = 'etapa-2.txt'
caminho_etapa_3 = 'etapa-3.txt'
caminho_etapa_4 = 'etapa-4.txt'
caminho_etapa_5 = 'etapa-5.txt'

# Lista para armazenar os dados processados
dados_processados = []

# Lendo o arquivo e processando os dados
with open(caminho_arquivo, 'r') as arquivo:
    # Ignora o cabeçalho
    arquivo.readline()
    
    # Lendo as linhas subsequentes
    for linha in arquivo:
        # Remove espaços extras e quebra de linha
        linha = linha.strip()
        
        # Dividindo a linha nos campos
        partes = linha.split(',')
        
        # Se o nome do ator tiver vírgulas, juntamos todas as partes até termos 6 elementos
        while len(partes) > 6:
            partes[0] += ',' + partes.pop(1)  # Junta o segundo elemento ao primeiro (nome do ator)

        # Atribuindo valores
        ator = partes[0].strip()
        faturamento_total = float(partes[1].strip())
        numero_filmes = int(partes[2].strip())
        media_por_filme = float(partes[3].strip())
        filme_top = partes[4].strip()
        faturamento_filme_top = float(partes[5].strip())
        
        # Adiciona os dados na lista
        dados_processados.append((ator, faturamento_total, numero_filmes, media_por_filme, filme_top, faturamento_filme_top))

# ** Etapa 1: Ator/Atriz com maior número de filmes **
ator_com_mais_filmes = max(dados_processados, key=lambda x: x[2])
with open(caminho_etapa_1, 'w') as arquivo_saida:
    arquivo_saida.write(f"{ator_com_mais_filmes[0]}: {ator_com_mais_filmes[2]} filmes")

# ** Etapa 2: Média de receita de bilheteria bruta dos principais filmes **
media_receita_filme_top = sum(d[5] for d in dados_processados) / len(dados_processados)
with open(caminho_etapa_2, 'w') as arquivo_saida:
    arquivo_saida.write(f"Média de receita bruta dos principais filmes: {media_receita_filme_top:.2f}")

# ** Etapa 3: Ator/Atriz com a maior média de receita de bilheteria bruta por filme **
ator_maior_media_por_filme = max(dados_processados, key=lambda x: x[3])
with open(caminho_etapa_3, 'w') as arquivo_saida:
    arquivo_saida.write(f"Ator/Atriz com a maior média de receita de bilheteria bruta por filme: {ator_maior_media_por_filme[0]} Média de receita por filme {ator_maior_media_por_filme[3]:.2f}")

# ** Etapa 4: Contagem de aparições dos filmes de maior bilheteria (#1 Movie) **
from collections import Counter

# Contando as aparições dos filmes de maior bilheteria (#1 Movie)
contagem_filmes_top = Counter(d[4] for d in dados_processados)

# Ordenando os filmes primeiro pela quantidade (decrescente) e depois pelo nome (alfabético)
filmes_ordenados = sorted(contagem_filmes_top.items(), key=lambda x: (-x[1], x[0]))

# Escrevendo o cabeçalho e a lista formatada no arquivo etapa-4.txt
with open(caminho_etapa_4, 'w') as arquivo_saida:
    # Escrevendo o cabeçalho
    arquivo_saida.write("Contagem de aparições dos filmes de maior bilheteria\n")
    
    # Escrevendo cada linha no formato solicitado
    for filme, contagem in filmes_ordenados:
        arquivo_saida.write(f"O filme {filme} aparece {contagem} vez(es) no arquivo\n")

# ** Etapa 5: Lista dos atores ordenada pela receita bruta total de bilheteria **
# Ordena os atores pela receita bruta total de bilheteria em ordem decrescente
atores_ordenados_receita = sorted(dados_processados, key=lambda x: -x[1])

# Escreve o cabeçalho e a lista formatada no arquivo etapa-5.txt
with open(caminho_etapa_5, 'w') as arquivo_saida:
    # Escrevendo o cabeçalho
    arquivo_saida.write("Lista dos atores ordenada pela receita bruta total de bilheteria\n")
    
    # Escrevendo cada ator no formato solicitado
    for ator, receita_total, *_ in atores_ordenados_receita:
        # Verifica se o nome do ator contém vírgula e adiciona aspas se necessário
        if ',' in ator:
            ator = f'"{ator}"'
        arquivo_saida.write(f"{ator} - {receita_total:.2f}\n")

