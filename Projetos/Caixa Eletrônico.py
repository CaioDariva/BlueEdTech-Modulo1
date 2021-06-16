# Projeto Caixa eletrônico
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois 
# informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
# existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota 
# de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, 
# quatro notas de 10, uma nota de 5 e quatro notas de 1.
quantidade100 = 0
quantidade50 = 0
quantidade10 = 0
quantidade5 = 0
quantidade1 = 0

quantidadesacar = float(input('Quantos você quer sacar? Insira um valor entre 10 e 600 reais.'))

while quantidadesacar < 10 or quantidadesacar > 600:
    quantidadesacar = float(input('Quantos você quer sacar? Insira um valor entre 10 e 600 reais.'))


quantidade_aux = quantidadesacar

quantidade100 = int(quantidade_aux // 100)
quantidade_aux = (quantidade_aux) - (quantidade100 * 100)

quantidade50 = int(quantidade_aux // 50)
quantidade_aux = (quantidade_aux) - (quantidade50 * 50)

quantidade10 = int(quantidade_aux // 10)
quantidade_aux = (quantidade_aux) - (quantidade10 * 10)

quantidade5 = int(quantidade_aux // 5)
quantidade_aux = (quantidade_aux) - (quantidade5 * 5)

quantidade1 = int(quantidade_aux // 1)
quantidade_aux = (quantidade_aux) - (quantidade1 * 1)

quantidade_total = int(quantidade100 + quantidade50 + quantidade10 + quantidade5 + quantidade1)

print(f'R$ {quantidadesacar:.2f} serão sacados de sua conta.')
print(f'A quantidade de notas totais será de {quantidade_total} notas com a seguinte distribuição:')

if quantidade100 > 0:
    print(f'{quantidade100} notas de 100.')
if quantidade50 > 0:
    print(f'{quantidade50} notas de 50.')
if quantidade10 > 0:
    print(f'{quantidade10} notas de 10.')
if quantidade5 > 0:
    print(f'{quantidade5} notas de 5.')
if quantidade1 > 0:
    print(f'{quantidade1} notas de 1.')