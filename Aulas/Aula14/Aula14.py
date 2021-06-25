# return

def area(num1,num2):
    '''area necessita de 2 argumentos para calcular a área de uma 
    figura geométrica bidimensional'''
    mult = num1 * num2
    return mult

print('Vamos calcular a área do seu terreno!')
print()
a = float(input('Digite a largura em metros: ').upper().replace(',' , '.').replace('M' , ''))
b = float(input('Digite o comprimento em metros: ').upper().replace(',' , '.').replace('M' , ''))
print()
print(area(a, b))

