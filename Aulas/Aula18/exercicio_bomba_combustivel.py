# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro.
# iii. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros
# que foi colocada no veículo.
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
# a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class Bomba_combustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel, quantidadeLitrosAbastecidos = 0):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        self.quantidadeLitrosAbastecidos = quantidadeLitrosAbastecidos

    def abastecerPorValor(self):
        valor = float(input('Quantos reais deseja abastecer? ').replace(',' , '.'))
        self.quantidadeLitrosAbastecidos = valor / self.valorLitro
        while self.quantidadeLitrosAbastecidos > self.quantidadeCombustivel:
            print(f'Não temos essa quatidade de combustível, temos apenas {self.quantidadeCombustivel} litros.')
            print()
            valor = float(input('Deseja abastecer quantos reais? '))
            self.quantidadeLitrosAbastecidos = valor / self.valorLitro
        print(f'Será abastecido {self.quantidadeLitrosAbastecidos:.2f} litros.')

    def abastecerPorLitro(self):
        self.quantidadeLitrosAbastecidos = float(input('Quantos litros? '))
        while self.quantidadeLitrosAbastecidos > self.quantidadeCombustivel:
            print(f'Não temos essa quatidade de combustível, temos apenas {self.quantidadeCombustivel:.2f} litros.')
            print()
            self.quantidadeLitrosAbastecidos = float(input('Deseja abastecer quantos litros? '))
        valorAbastecido = self.quantidadeLitrosAbastecidos * self.valorLitro
        print(f'O valor será de {valorAbastecido}')

    def alterarCombustivel(self):
        comb = str(input('Qual combustível será usado? Alcool ou Gasolina?')).lower().replace(' ' , '').replace('á' , 'a')
        if comb == 'gasolina':
            self.tipoCombustivel = 'gasolina'
            return self.tipoCombustivel
        elif comb == 'alcool':
            self.tipoCombustivel = 'alcool'
            return self.tipoCombustivel

    def alterarValor(self):
        if self.tipoCombustivel == 'gasolina':
            print('O valor da gasolina é de R$ 5,50 por litro.')
            self.valorLitro = 5.50
            return self.valorLitro
        elif self.tipoCombustivel == 'alcool':
            print('O valor do alcool é de R$ 4,50 por litro.')
            self.valorLitro = 4.50
            return self.valorLitro
    
    def alterarQuantidadeCombustivel(self):
        self.quantidadeCombustivel -= self.quantidadeLitrosAbastecidos

abastecimento = Bomba_combustivel('alcool', 4.50, 500)
while True:
    abastecimento.alterarCombustivel()
    print()
    abastecimento.alterarValor()
    print()
    tipoabastecimento = str(input('Deseja abastecer por litro ou por valor? ')).lower().replace(' ' , '')
    if tipoabastecimento == 'litro':
        abastecimento.abastecerPorLitro()
    elif tipoabastecimento == 'valor':
        abastecimento.abastecerPorValor()
    print()
    abastecimento.alterarQuantidadeCombustivel()
    continuacao = input('Deseja abastecer outro veículo?')
    print()
    if continuacao != 'sim' and continuacao != 'nao':
         continuacao = input('Deseja abastecer outro veículo? Sim ou não?').lower().replace(' ' , '').replace('ã' , 'a')
    elif continuacao =='nao':
        break
print(f'Ainda restou na bomba {abastecimento.quantidadeCombustivel:.2f} litros.')

# Depois devemos proteger os atributos, tipo, valor por tipo e quantidade, para nao acessarem.