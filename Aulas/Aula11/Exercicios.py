# # 2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados 
# # em uma lista) e seus valores correspondentes aos quadrados desses números.

# numeros = {1 : 1, 4 : 16, 5 : 25, 6 : 36, 7 : 49, 9 :81}

# #b – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor 
# # associado é o número ao quadrado.​

# dicionario = dict()
# for i in range(1, 11):
#     dicionario[i] = i**2

# print(dicionario)



### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

estoque = {'Papel' : 20, 'Coca' : 15, 'Batata' : 10, 'Cenoura' : 50, 'Chocolate' : 5}
produto = input('O que você quer comprar? ')
quantidade = int(input('Quantidade: '))

retirada = (estoque.pop((produto - quantidade), 'Não encontrado na lista'))




# produtos = input('O que você gostaria de comprar: ')
# quantidade = int(input('Qual quantidade: '))
# compra = estoque.get(produtos, 'Produto Inválido')
# compra_total = estoque.pop(quantidade, 'Quantidade indisponível')
# print(compra)
# print(compra_total)
# print(estoque)
# retirada = estoque(produtos)