## 1 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
## Caso esteja errado, peça a digitação novamente até ter um valor correto.

# sexo = str(input('Qual é o seu sexo? F ou M? \n')).upper()

# while (sexo != 'M') and (sexo != 'F'):
#   sexo = str(input('Errado. Qual é o seu sexo? F ou M? \n')).upper()
# if sexo == 'F':
#   print('Seu sexo é feminino!')
# elif sexo == 'M':
#   print('Seu sexo é masculino!')




## 2 - Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem corretamente 
## a senha. A senha é “Blue123” 2b - Exiba quantas vezes o usuário errou a digitação.

# senha = 'Blue123'
# entrada = input("Digite a senha:")
# erros = 0

# while entrada != senha:
#     erros += 1
#     entrada = input('Incorreta.\nDigite Novamente: ')
#     if senha == entrada:
#         break
# print('Bem Vindo!')
# print(f'Você errou: {erros} vezes.')




## 3 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa 
## deverá perguntar se o usuário quer ou não continuar. No final, mostre:
## A) Quantas pessoas tem mais de 18 anos. 
## B) Quantos homens foram cadastrados. 
## C) Quantas mulheres tem menos de 20 anos.

# pmais18 = 0
# mmenos20 = 0
# htotal = 0

# idade = int(input('Qual sua idade?'))
# sexo = str(input('Qual é o seu sexo? Digite F ou M.')).upper()
# while (sexo != 'M') and (sexo != 'F'):
#     sexo = str(input('Por favor, digite F ou M?')).upper()

# if idade > 18:
#     pmais18 += 1

# if sexo == 'M':
#     htotal += 1

# if (sexo == 'F') and (idade < 20):
#     mmenos20 += 1

# cont = str(input('Deseja continuar? Sim ou não?')).replace(' ' , '').upper().replace('Ã' , 'A')
# while (cont != 'SIM') and (cont != 'NAO'):
#     cont = str(input('Deseja continuar? Sim ou não?')).replace(' ' , '').upper().replace('Ã' , 'A')

# if cont == 'NAO':
#     print(f'Ok, {pmais18} pessoas possuem mais de 18 anos, {htotal} homens foram cadastrados e {mmenos20} mulheres tem menos de 20 anos!')

# while cont == 'SIM':
#     idade = int(input('Qual sua idade?'))
#     sexo = str(input('Qual é o seu sexo? Digite F ou M.')).upper()
#     while (sexo != 'M') and (sexo != 'F'):
#         sexo = str(input('Por favor, digite F ou M?')).upper()

#     if idade > 18:
#         pmais18 += 1

#     if sexo == 'M':
#         htotal += 1

#     if (sexo == 'F') and (idade < 20):
#         mmenos20 += 1

#     cont = str(input('Deseja continuar? Sim ou não?')).replace(' ' , '').upper().replace('Ã' , 'A')
#     while (cont != 'SIM') and (cont != 'NAO'):
#         cont = str(input('Deseja continuar? Sim ou não?')).replace(' ' , '').upper().replace('Ã' , 'A')

#     if cont == 'NAO':
#         print(f'Ok, {pmais18} pessoas possuem mais de 18 anos, {htotal} homens foram cadastrados e {mmenos20} mulheres tem menos de 20 anos!')




## DESAFIO:
## 4 - Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar 
## qual número foi escolhido até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

num_sorteado = random.randint(0, 10)
palpites_errados = 0

palpite_dado = int(input('O computador sorteou um número de 0 a 10, tente acertá-lo!'))
while palpite_dado != num_sorteado:
  palpites_errados += 1
  palpite_dado = int(input('Errou! Tente novamente: '))
if palpite_dado == num_sorteado:
    print(f'Parabéns você acertou e errou {palpites_errados} vezes.')