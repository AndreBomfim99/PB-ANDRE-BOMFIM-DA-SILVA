from collections import Counter
caminho_arquivo = 'actors.csv'
caminho_etapa_4 = 'etapa-4.txt'
dados_processados = []

with open(caminho_arquivo, 'r') as arquivo:
    arquivo.readline()
    for linha in arquivo:
        linha = linha.strip()
        partes = linha.split(',')
        while len(partes) > 6:
            partes[0] += ',' + partes.pop(1)
        filme_top = partes[4].strip()
        dados_processados.append(filme_top)

contagem_filmes_top = Counter(dados_processados)
filmes_ordenados = sorted(contagem_filmes_top.items(), key=lambda x: (-x[1], x[0]))
with open(caminho_etapa_4, 'w') as arquivo_saida:
    arquivo_saida.write("Contagem de aparições dos filmes de maior bilheteria\n")
    for filme, contagem in filmes_ordenados:
        arquivo_saida.write(f"O filme {filme} aparece {contagem} vez(es) no arquivo\n")
