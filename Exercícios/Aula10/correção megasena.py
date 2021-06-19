## Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
## O programa vai perguntar quantos jogos serão gerados e vai sortear 6
## números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

### 
### Ideia é ir por partes, 1primeiro cria o input, 2depois faz o codigo para pegar 1 numero entre 1 e 60 aleatório,
### e faz repetir ele 6 vezes com o for, 3após isso precisamos colocar todos os 6 valores dentro uma lista, 4agora 
### mandamos apenas adicionar na lista se for número novo, 5mas ai se for novo vai contar a iteração e nao vai 
### adiconar nada então while para conseguir 6 aleatórios sem erro, agora for i in range para repetir quantas vezes
### for da entrada do usuario, a lista jogo tem que estar dentro do for para zerar todas vez que passar pelo while
### se não, repete toda a lista o tanto de vezes que o usuario colcoar.
### 


from random import randint   # para importar só a função randint exemplo: num = randint(1 , 60) nao precisa random

jogos_total = list()

quantidade_jogos = int(input('Quantos jogos você quer gerar? '))

for i in range(quantidade_jogos):
    jogo = list()
    while len(jogo) < 6:                    #for numero in range (6): - como estava antes
        num = randint(1 , 60)
        if num not in jogo:
            jogo.append(num)       
    jogos_total.append(jogo[:])   #[:] serve para criar uma cópia da lista dentro da outra, para que se a lista for manipulada nao altere dentro da lista maior

print('Seus jogos: ')
# print(jogos_total)

# aqui o for vai percorrer o numero de listas dentro das listas, cada ve que o j rodar vai receber o elemento

contador = 0
for j in jogos_total:
    contador += 1
    print(f' Jogo {contador}: {j}') # vai printar um em cada linha 