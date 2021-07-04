class Pessoa:
    def __init__(self, olhos, altura, peso, idade):
        self.olhos = olhos
        self.altura = altura
        self.peso = peso
        self.idade = idade

    def envelhecer(self, anos = 1):
        self.idade += anos

class Medico(Pessoa):
    def __init__(self,olhos, altura, peso, idade, crm):
        super().__init__(olhos, altura, peso, idade)
        self.crm = crm

    def medicar(self):
        print('Receitar remédio.')

    def trabalhar(self):
        print('Trabalha no consultorio')
    
class Neuro(Medico):
    def __init__(self,olhos, altura, peso, idade, crm, especialidade):
        super().__init__(olhos, altura, peso, idade, crm)
        self.especialidade = especialidade

class Advogado(Pessoa):
    def __init__(self,olhos, altura, peso, idade, oab):
        super().__init__(olhos, altura, peso, idade)
        self.oab = oab

    def advogar(self):
        print('Eu advogo.')

    def trabalhar(self):
        print('Trabalha no escritorio')

pessoa = Pessoa('castanho', 1.8, 80, 20)

medico = Medico('castanho', 1.8, 80, 20, '123456')

neuro = Neuro('castanho', 1.8, 80, 20, '123456', 'Cérebro')

advogado = Advogado('azul', 1.90, 85, 25, '654321')

print(pessoa.idade)     
pessoa.envelhecer(5)
print(pessoa.idade)
pessoa.envelhecer()             # envelhecer é método de pessoa
print(pessoa.idade)

print()

print(medico.idade)
medico.envelhecer()
print(medico.idade)             # no medico uso método envelhecer e o método medicar
medico.medicar()
medico.trabalhar()              #polimorfismo é isso, tem trabalhar no medico e no advogado, mas sao diferentes

print()

print(neuro.idade)
neuro.envelhecer()
print(neuro.idade)              # no neuro so método envelhecer e método medicar também
neuro.medicar()
neuro.trabalhar()

print()

print(advogado.idade)
advogado.envelhecer(3)
print(advogado.idade)
advogado.trabalhar()

print(vars(pessoa))

print()

print(vars(medico))

print()

print(vars(neuro))

print()

print(vars(advogado))