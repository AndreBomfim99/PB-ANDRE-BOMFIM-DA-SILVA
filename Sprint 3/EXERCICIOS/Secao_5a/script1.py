caminho_arquivo = 'actors.csv'
caminho_etapa_1 = 'etapa-1.txt'
dados_processados = []

with open(caminho_arquivo, 'r') as arquivo:
    arquivo.readline()  
    for linha in arquivo:
        linha = linha.strip()
        partes = linha.split(',')
        while len(partes) > 6:
            partes[0] += ',' + partes.pop(1)
        ator = partes[0].strip()
        faturamento_total = float(partes[1].strip())
        numero_filmes = int(partes[2].strip())
        media_por_filme = float(partes[3].strip())
        filme_top = partes[4].strip()
        faturamento_filme_top = float(partes[5].strip())
        dados_processados.append((ator, faturamento_total, numero_filmes, media_por_filme, filme_top, faturamento_filme_top))

ator_com_mais_filmes = max(dados_processados, key=lambda x: x[2])
with open(caminho_etapa_1, 'w') as arquivo_saida:
    arquivo_saida.write(f"{ator_com_mais_filmes[0]}: {ator_com_mais_filmes[2]} filmes")
