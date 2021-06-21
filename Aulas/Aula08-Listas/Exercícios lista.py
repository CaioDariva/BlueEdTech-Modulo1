## 1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações: 
## a) tamanho da lista. 
## b) maior valor da lista. 
## c) menor valor da lista. 
## d) soma de todos os elementos da lista. 
## e) lista em ordem crescente. 
## f) lista em ordem decrescente.

l = [5, 7, 2, 9, 4, 1, 3]

taml = len(l)
mav = max(l)
mev = min(l)
somaL = sum(l)
cres = sorted(l)
dec = sorted(l, reverse=True)

print(f'A lista é {l}.')
print(f'A lista possui {taml} elementos.')
print(f'O maior valor da lista é {mav}.')
print(f'O menor valor da lista pe {mev}')
print(f'A soma de todos os elementos é {somaL}.')
print(f'A lista em ordem crescente é {cres}.')
print(f'A lista em ordem decrescente é {dec}.')

## 2- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
## As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" 
## "Devia para a vítima?" "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação 
## sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser 
## classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será 
## classificado como "Inocente".
## Mesmo exercício do desafio, mas agora com lista, vamos pensar como seria.



## 3- Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma 
## aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
