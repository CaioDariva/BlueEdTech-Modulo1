# Basico de classe:

class Mamifero:
    def __init__(self, nome, pelo, cor, tamanho, idade):
        self.nome = nome
        self.pelo = pelo
        self.cor = cor
        self.tamanho = tamanho
        self.idade = idade

    def crescer(self):
        self.idade += 1

    def locomover(self):
        print('Ele está andando')

    def comer(self):
        self.tamanho = 'grande'


cachorro = Mamifero('Amy', 'curto', 'preto', 'médio', 2 )
print(type(cachorro))
print(vars(cachorro))
print(type(vars(cachorro)))

print()

cachorro.crescer()
cachorro.locomover()
cachorro.comer()
print(vars(cachorro))

print(cachorro.nome)