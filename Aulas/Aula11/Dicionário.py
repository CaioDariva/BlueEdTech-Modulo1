# enumerate

# lista = [10, 20, 30, 40, 50]

# for m in (lista):
#     print(m)

# print()

# for l in range(len(lista)):
#     print(l)

# print()

# for i, j in enumerate(lista): #pega índice e elemento, da para criar tuplas com ,
#     print(i)
#     print(j)

## Até aqui revisão de lista, agora Dicionário.

# lista = [('caio', '3333-4444'), ('let', '2222-5555'), ('abc', '1111-2222'), ('joao', '1234-1234'), ('tuts', '2345-3456')]

# contatos = dict(lista) # transformando em dicionario desde que a lista esteja organizada em pares como em cima
# print(contatos)
# print()
# print(contatos['caio'])
# print()
# print(contatos.get('Caio', 'Não encontrado!')) #get é igual o print, porém se não tem a chave, nao quebra o programa no caso nao tem Caio
# print()
# nome = input('Digite um nome: ')
# print()
# print(contatos.get(nome, 'Não encontrado!'))

# dic_avengers = {'Chris Evans':'Capitão América', 'Mark Ruffalo':'Hulk', 'Tom Hiddleston':'Loki', 'Chris Hemsworth':'Thor', 'Robert Downey Jr':'Homem de Ferro', 'Scarlett Johansson':'Viúva Negra'}
# print(type(dic_avengers))

# print()

# print('Hulk' in dic_avengers.values())
# print('Tom Hiddleston' in dic_avengers.keys())
# print('Hulk' in dic_avengers.values() and 'Tom Hiddleston' in dic_avengers.keys())

# print()

# print(dic_avengers)
# dic_avengers["Tom Holland"] = "Homem aranha" #Adicionar chaves e valores 

# print()

# print(dic_avengers)

# print()

# ator = input('Digite um ator: ')
# personagem = input('Digite um personagem: ')
# dic_avengers[ator] = personagem

# print()

# print(dic_avengers)

# print()

# del dic_avengers['Tom Holland']

# print()

# print(dic_avengers)

# print()
#pop

dic_avengers = {'Chris Evans':'Capitão América', 'Mark Ruffalo':'Hulk', 'Tom Hiddleston':'Loki', 'Chris Hemsworth':'Thor', 'Robert Downey Jr':'Homem de Ferro', 'Scarlett Johansson':'Viúva Negra'}
print(type(dic_avengers))

deletados = dic_avengers.pop('Chris Evans')

print(dic_avengers)
print()
print(deletados)
print()
ator = input('Digite um ator para deletar: ')
del_usuario = dic_avengers.pop(ator, 'Não encontrado na lista')
print()
print(dic_avengers)
print()
print(del_usuario)
print()
ator = input('Digite um ator para deletar: ')
print(dic_avengers.pop(ator, 'Não encontrado na lista'))
print()
print(dic_avengers)