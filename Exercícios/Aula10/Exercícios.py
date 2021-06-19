## 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, 
## verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a 
## seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  
## também quantos são maiores e quantos são menores de idade.

lista_geral = list()

for i in range(5):
    lista = list()
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite a idade: '))
    lista.append(nome)
    lista.append(idade)
    lista_geral.append(lista)

print(lista_geral)

contador = 0
qntdmaiores = 0
qntdmenores = 0

for j in lista_geral:
    if lista_geral [contador][1] >= 18:
        print(f'{lista_geral[contador][0]} é maior de idade')
        contador += 1
        qntdmaiores += 1
    elif lista_geral[contador][1] < 18:
        print(f'{lista_geral[contador][0]} é menor de idade')
        contador += 1
        qntdmenores += 1


print()
print(f'{qntdmenores} são menores de idade')
print(f'{qntdmaiores} são maiores de idade')