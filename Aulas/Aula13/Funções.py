# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno:

def area(num1,num2):
    '''area necessita de 2 argumentos para calcular a área de uma 
    figura geométrica bidimensional'''
    mult = num1 * num2
    print(f'A área do seu terreno é: {mult:.2f}m².')

print('Vamos calcular a área do seu terreno!')
print()
a = float(input('Digite a largura em metros: ').upper().replace(',' , '.').replace('M' , ''))
b = float(input('Digite o comprimento em metros: ').upper().replace(',' , '.').replace('M' , ''))
print()
area(a,b)