import random
import time
import os
import names

# set dos parâmetros
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# gera nomes
aux = []
print("Gerando nomes únicos: ")
for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios...")
dados = []
for i in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

caminho_arquivo = r"C:\EXE_GERACAO\geranomes\nomes_aleatorios.txt"
print(f"Salvando nomes no arquivo: {caminho_arquivo}")
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for nome in dados:
        arquivo.write(nome + "\n")


