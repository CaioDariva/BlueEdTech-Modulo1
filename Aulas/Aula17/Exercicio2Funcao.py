# Desafio 2 - Vamos aprimorar o código:  cadastro de jogador de futebol.py que foi desenvolvido no Code Lab 
# da aula 14. Faça com que o seu código funcione para vários jogadores, incluindo um sistema de visualização 
# de detalhes de aproveitamento de cada jogador.



class futebol():
    def __init__ (self,nome, partida, gols):
        self.nome = nome
        self.partida = partida
        self.gols = gols

    def aproveitamento(self):
        soma = sum(lgols)
        res = soma / self.partida
        fut.append([self.nome, self.partida, soma, res])
        


fut =[]

while True:
    lgols = []
    n = input('Nome do jogador: ')
    qp = int(input('Quantas partidas: '))
    for i in range(qp):
        qg = int(input(f'Quantos gols na partida {i+1}º: '))
        lgols.append(qg)
    jog = futebol(n,qp,qg)
    jog.aproveitamento()
    addnovo = input('Deseja adicionar mais um jogador? ')
    if addnovo == 'n':
        break
    
for i in fut:
    print(f'O jogador {i[0]} jogou {i[1]} partida(s), fez o total de {i[2]} gol(s) e sua média de gols por partida foi {i[3]}.')