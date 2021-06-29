# 2) Crie uma classe chamada Conta para simular as operações de
# uma conta corrente. Sua classe deverá ter os atributos Titular e
# Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
# Conta e teste os atributos e métodos implementados.

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self):
        saque = int(input('Quanto será sacado? '))
        while saque > self.saldo:
            saque = int(input('Indisponível, tente outro valor: '))
        self.saldo -= saque
        
    
    def depositar(self):
        deposito = int(input('Quanto será depositado? '))
        self.saldo += deposito

nome = input('Nome: ')
saldo = 1000
objeto = Conta(nome, saldo)
continuacao = 'sim'
while continuacao == 'sim':
    print(f'Seu saldo é {objeto.saldo}.')
    operacao = input('Você deseja sacar ou depositar?').lower()
    if operacao == 'sacar':
        objeto.sacar()
    elif operacao == 'depositar':
        objeto.depositar()
    continuacao = input('Deseja fazer outra operacao? Sim ou Não?').lower().replace(' ' , '').replace('ã' , 'a')
    if continuacao == 'nao':
        pass
print()

print(f'A operação foi realizada e o seu saldo é: {objeto.saldo}')