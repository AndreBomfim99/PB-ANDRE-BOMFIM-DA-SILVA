# Exercício 11
# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
# Dica: leia a documentação do pacote json

import json

with open('person.json', 'r') as file:
    data = json.load(file)
print(data)