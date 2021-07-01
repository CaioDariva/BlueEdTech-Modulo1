# quando não quer que o usuário acesse certos atributos
# nos podemos acessar qualquer informação de qualquer lugar, com encapsulamento é necessario usar um metodo para
# acessar (get - set)
# basicamente é criar metodos para acessar os atributos
# devemos indicar os atributos que nao devem ser acessados sem um metodo com 2 underlines, porem isso 
# só indica, nao impede o acesso 

class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0

    @property # cria um metodo que é chamado como atributo
    def salario(self):
        return self.__salario    

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada



eduardo = Funcionario('Eduardo', 'Dev Senior', 100)
print(vars(eduardo))
print()
eduardo.registra_hora_trabalhada()
eduardo.registra_hora_trabalhada()
eduardo.calcula_salario()
print(vars(eduardo))
print()
print(eduardo.salario) #criado o salario apenas para ser chamado, é chamdo comoa tributo mas ele nao é