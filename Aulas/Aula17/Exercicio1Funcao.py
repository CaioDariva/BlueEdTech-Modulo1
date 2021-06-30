# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, crie um lançador de dados e 
# moedas em que o usuário deve escolher o objeto a ser lançado. Não esqueça que os lançamentos são feitos de 
# forma randômica.

from random import randint

class Lancador():
    def __init__(self, lados):
        self.lados = lados

    def lancar(self):
       if self.lados = 2:
           sorteio = randint(0, 1)

escolha = str(input('escolha dado ou moeda: '))
player = Lancador(escolha)
player.lancar()

