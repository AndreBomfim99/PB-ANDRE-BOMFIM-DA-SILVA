caminho_arquivo = 'actors.csv'
caminho_etapa_5 = 'etapa-5.txt'
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
        dados_processados.append((ator, faturamento_total))

atores_ordenados_receita = sorted(dados_processados, key=lambda x: -x[1])
with open(caminho_etapa_5, 'w') as arquivo_saida:
    arquivo_saida.write("Lista dos atores ordenada pela receita bruta total de bilheteria\n")
    for ator, receita_total in atores_ordenados_receita:
        if ',' in ator:
            ator = f'"{ator}"'
        arquivo_saida.write(f"{ator} - {receita_total:.2f}\n")
