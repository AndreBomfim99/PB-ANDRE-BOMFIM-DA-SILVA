#CÓDIGO PARA MASCARAR COM HASH

import hashlib

while True:
    entrada = input("Digite algo para mascarar ou digite sair: ")
    if entrada.lower() == 'sair':
        break
    hasheador = hashlib.sha1(entrada.encode())
    print("Hash SHA-1:", hasheador.hexdigest())
