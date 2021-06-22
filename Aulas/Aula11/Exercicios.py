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

estoque = {'TOMATE' : 10, 'ARROZ' : 10, 'BATATA' : 10, 'CENOURA' : 10, 'CHOCOLATE' : 10, 'LEITE' : 10}

continuação = 'SIM'

compra = dict()
compra2 = list()

print('Bem-vindo ao Mercado!')
print()

while continuação == 'SIM':
    produto = str(input('O que você gostaria de comprar? ')).upper()
    print()
    while produto not in estoque:
        print('Produto inválido.')
        produto = input('O que você gostaria de comprar? ').upper()
        print()
    retirada = int(input('Qual a quantidade? '))
    quantidade = estoque.pop(produto)


    while retirada > quantidade and quantidade != 0:
        print(f'Quantidade indisponível. Possuímos apenas {quantidade} unidades.')
        retirada = int(input('Quantas você deseja? '))


    if retirada <= quantidade:
        compra[produto] = retirada
        compra2.append(retirada)
        estoque[produto] = (quantidade - retirada)


    while quantidade == 0:
        produto = input(f'Esse produto acabou.\nNós ainda temos {estoque}.\nPor favor escolha outro: ').upper()
        while produto not in estoque:
            print('Produto inválido.')
            print()
            produto = input('O que você gostaria de comprar? ').upper()
            print()
        retirada = int(input('Qual a quantidade? '))
        quantidade = estoque.pop(produto)
        while retirada > quantidade:
            print(f'Quantidade indisponível. Possuímos apenas {quantidade} unidades.')
            retirada = int(input('Quantas você deseja? '))
        if retirada <= quantidade:
            compra[produto] = retirada
            compra2.append(retirada)
            estoque[produto] = (quantidade - retirada)


    print()

    continuação = str(input('Você deseja comprar mais itens? ')).upper().replace('Ã' , 'A')
    while continuação != 'SIM' and continuação != 'NAO':
        continuação = str(input('Você deseja comprar mais itens, sim ou não? ')).upper().replace('Ã' , 'A')

print()


if continuação == 'NAO':
    print('Obrigado pelas compras.')
    print()
    print(f'Você adquiriru {len(compra)} tipos de itens diferentes e um total de {sum(compra2)} unidades')