def le_numbertxt(number_txt):
    with open(number_txt, "r") as txt:
        return [int(line.strip()) for line in txt]


number_txt = "number.txt"

numeros = le_numbertxt(number_txt)  

maiores_PAR = sorted(filter(lambda x: x % 2 == 0, numeros), reverse=True)[:5]  
maiores_PAR = list(map(int, maiores_PAR))  

soma = sum(maiores_PAR)

print(maiores_PAR)
print(soma)