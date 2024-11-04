caminho_arquivo = 'actors.csv'
caminho_etapa_3 = 'etapa-3.txt'
dados_processados = []

with open(caminho_arquivo, 'r') as arquivo:
    arquivo.readline()
    for linha in arquivo:
        linha = linha.strip()
        partes = linha.split(',')
        while len(partes) > 6:
            partes[0] += ',' + partes.pop(1)
        ator = partes[0].strip()
        media_por_filme = float(partes[3].strip())
        dados_processados.append((ator, media_por_filme))

ator_maior_media_por_filme = max(dados_processados, key=lambda x: x[1])
with open(caminho_etapa_3, 'w') as arquivo_saida:
    arquivo_saida.write(f"Ator/Atriz com a maior média de receita por filme: {ator_maior_media_por_filme[0]} Média de receita por filme {ator_maior_media_por_filme[1]:.2f}")
