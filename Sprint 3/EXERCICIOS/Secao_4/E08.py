# Exercício 8
# Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
# Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
# É necessário que você imprima no console exatamente assim:
# A palavra: maça não é um palíndromo
# A palavra: arara é um palíndromo

palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 

def palindromo(palavra):
    return palavra == palavra[::-1]
    
for palavra in palavras:
    if palindromo(palavra):
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")