## 01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
## cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
## adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
## crescente.


# num = list() # Variável criada como lista

# while True:
#     n = int(input('Informe um número: ')) 
#     if n not in num: # Se o valor digitado não estiver na lista ele é adicionado com o append
#         num.append(n)
#     else:           ## se ja estiver na lista ele não adiciona
#         print('Valor ja está na lista ') 
#     resposta = str(input('Deseja continuar: [S/N]' )) # aqui é a condição de parada se a resposta "N ou n"
#     if resposta in 'Nn':
#         break
    
# print(num) # print lista completa
# num.sort() # Odernando a lista
# print(num) # print lista ordenada



## 02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
## disso, crie duas listas extras que vão conter apenas os valores pares e os valores
## ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
## geradas.


# par = list() 
# impar = list()
# lista = list()

# while True:
#     lista.append(int(input('Digite um valor: ')))
#     resposta = str(input('Deseja continuar: [S/N]' ))
#     if resposta in 'Nn':
#         break
   
# for n in lista: 

#     if  n %2 == 0:
#         par.append(n)
        
#     else:
#         impar.append(n)
        
# print(par)
# print(impar)



## Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
## palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
## números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# import random
# n1 = random.randint(1,60)
# n2 = random.randint(1,60)
# n3 = random.randint(1,60)
# n4 = random.randint(1,60)
# n5 = random.randint(1,60)
# n6 = random.randint(1,60)


# num_jogos = 0
# lista = list()
# n = random.randint(1,60)

# for i in range(0,5):
#     lista.apend(i)

# print(lista)
# -------------------------


import random

cont = 0
cont2 = 0
jogo = list()
num_jogos = 0


while True:
    n = random.randint(1,60)
    if cont <= 5:
        if n not in jogo:
            cont += 1
            jogo.append(n)
    else:
        break
jogo.sort()




print(jogo)