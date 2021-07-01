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
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self):
        valor = float(input('Quantos reais? '))
        quantidadeAbastecidaValor = valor / self.valorLitro
        return quantidadeAbastecidaValor

    def abastecerPorLitro(self):
        litros = float(input('Quantos litros? '))
        quantidadeAbastecidaLitro = litros / self.valorLitro
        return quantidadeAbastecidaLitro

    def alterarValor(self):
        self.valorLitro = 

    def alterarCombustivel(self):

    def alterarQuantidadeCombustivel(self):

alcool = 4.50
gasolina = 5.50

# Depois devemos proteger todos os atributos, tipo, valor por tipo e quantidade, para nao acessarem.