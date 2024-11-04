# Exercício 15: Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:

# liga(): muda o estado da lâmpada para ligada
# (): muda o estado da lâmpada para desligada
# esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

# Para testar sua classe:

# Ligue a Lampada

# Imprima: A lâmpada está ligada? True

# Desligue a Lampada

# Imprima: A lâmpada ainda está ligada? False

class Lampada:
    def __init__ (self, ligada= False):
        self.ligada = ligada
    def liga(self):
        self.ligada = True
    def desliga(self):
        self.ligada = False
    def esta_ligada(self):
        return self.ligada
    
lampada = Lampada()

lampada.liga()
print ('a lampada ligou!')

print (f'a lampada está ligada? {lampada.esta_ligada()}')

lampada.desliga()
print('a lampada desligou')

print (f'a lampada continua ligada? {lampada.esta_ligada()}')
