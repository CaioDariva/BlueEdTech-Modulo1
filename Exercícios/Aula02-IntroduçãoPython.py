print('Criação de variáveis, seus tipos e uso do print') 
var1 = "Blue"
var2 = 15
var3 = 1.45
var4 = True

print()

print('Variáveis:')
print(var1)
print(var2)
print(var3)
print(var4)

print() 

print('Tipos conforme as variáveis acima:')
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

print()

print('Como criar várias variáveis: ')
print('var_1, var_2, var_3, var_4 = 10, 1.4, "blue", True ==> dará as seguintes variáveis: ')
var_1, var_2, var_3, var_4 = 10, 1.4, "blue", True
print(var_1)
print(var_2)
print(var_3)
print(var_4)

print()

print('printar várias variáveis')
print('print(var_1, var_2, var_3, var_4)')

print()

print('Só é possível fazer operações com variáveis compatíveis')

print('Criar inputs')
nome = str(input("Digite o seu nome: "))
num1 = int(input("Digite o seu número: "))
print(nome)
print(num1)

print()

print('Usamos int, float, str e bool para tornar a variável no tipo que desejar')

print()

# Operadores Aritméticos + - * /
# // é divisão inteira
# ** exponenciação
# % resto da divisão

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Soma é: ", num1 + num2)
print("Subtração é: ", num1 - num2)
print("Multiplicação é: ", num1 * num2)
print("Divisão é: ", num1 / num2)
print("Divisão inteira é:", num1 // num2)
print("Exponenciação é: ", num1 ** num2)
print("Resto da divisão é: ", num1 % num2)

