caminho_arquivo = 'actors.csv'
caminho_etapa_2 = 'etapa-2.txt'
dados_processados = []

with open(caminho_arquivo, 'r') as arquivo:
    arquivo.readline()
    for linha in arquivo:
        linha = linha.strip()
        partes = linha.split(',')
        while len(partes) > 6:
            partes[0] += ',' + partes.pop(1)
        faturamento_filme_top = float(partes[5].strip())
        dados_processados.append(faturamento_filme_top)

media_receita_filme_top = sum(dados_processados) / len(dados_processados)
with open(caminho_etapa_2, 'w') as arquivo_saida:
    arquivo_saida.write(f"Média de receita bruta dos principais filmes: {media_receita_filme_top:.2f}")
