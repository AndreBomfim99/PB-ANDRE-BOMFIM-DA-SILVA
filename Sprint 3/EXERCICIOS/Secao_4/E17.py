# Exercício 17: Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 

def divisao_lista(lista):
    tamanho = len(lista) // 3

    parte1 = lista[:tamanho]
    parte2 = lista[tamanho : 2 * tamanho]
    parte3 = lista[2 * tamanho :]

    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = divisao_lista(lista)

print(parte1, parte2, parte3)