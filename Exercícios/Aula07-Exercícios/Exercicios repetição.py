## Execute as atividades abaixo, utilizando a estruturade repetição FOR:


## 01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


# menor = 0
# maior = 0

# for i in range(1,6):
#     peso = float(input('Digite o peso: ').replace(',' , '.'))
#     if i == 1:
#         menor = peso
#         maior = peso
#     else:
#         if peso < menor:
#             menor = peso
#         if peso > maior:
#             maior = peso
# print(f'O peso menor foi de {menor} e o peso maior foi de {maior}')





## 02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.


# num = (int(input('Digite um número para saber sua tabuada: ')))

# for i in range(1 , 11):
#     valor = i * num
#     print(f'{i} x {num} = {valor}')




## 03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda 
## não atingiram a maioridade e quantas já são maiores.

# maiores = 0
# menores = 0

# for i in range(1 , 8):
#     ano = int(input('Que ano você nasceu?'))
#     if ano > 2003:
#         menores += 1
#     else:
#         maiores += 1
# print(f'{maiores} pessoas atingiram a maioridade e {menores} pessoas ainda não atingiram')




## 04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
## Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.

# soma = 0
# qntd_pares = 0

# for i in range(1, 7):
#     num = (int(input('Digite um número inteiro para somar os pares: ')))
#     if num % 2 == 0:
#         soma = soma + num
#         qntd_pares += 1

# print(f'A soma é {soma} e foram digitados {qntd_pares}')



## Execute as atividades abaixo, utilizando a estruturade repetição WHILE:
## 01- Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar 
## [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa Seu programa deverá realizar a operação solicitada 
## em cada caso. (utilizar while sem break)





## 02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
## perguntar se o usuário quer ou não continuar. No final, mostre: 
## A) Quantas pessoas têm mais de 18 anos. 
## B) Quantos homens foram cadastrados. C) Quantas mulheres têm menos de 20 anos.



## 03 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário 
## vai continuar ou não. No final, mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam mais de 
## R$1000. (C) Qual é o nome do produto mais barato.


## DESAFIOS
## 01 Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual 
## número foi escolhido até acertar, entre os palpites diga ao jogador se o número do computador é maior ou 
## menor ao que ele digitou,no final mostre quantos palpites foram necessários para vencer.


## 02 Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
## Os códigos utilizados são: 1, 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela 
## ex: 1 - José / 2- João / etc) # 5 - Voto Nulo # 6 - Voto em Branco 
## Faça um programa que calcule e mostre: 
## O total de votos para cada candidato; 
## O total de votos nulos; 
## O total de votos em branco; 
## A percentagem de votos nulos sobre o total de votos; 
## A percentagem de votos em branco sobre o total de votos.