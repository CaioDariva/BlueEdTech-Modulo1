# Módulo é pegar uma função de outro arquivo no caso o módulo

# from exemplo_calcular import calcular #from arquivo import função -> Quando quero importar apenas funções específicas
import calcular # importa todas as funções do arquivo
# import exemplo_calcular as ex #i mporta o arquivo inteiro com um "apelido" para ser chamado.

entradas = []
for i in range(5):
    numero = int(input("Entre um número: "))
    entradas.append(numero)

operador = input("Digite a operação que deseja: ")

# a = calcular(entradas,operador) #funciona se eu tiver importado apenas essa função (método 1 lá em cima - "from exemplo import...")
a = calcular.calcular(entradas,operador)
print(a)