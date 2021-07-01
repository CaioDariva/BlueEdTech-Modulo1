class Guerreiro:
    def __init__(self, atk, defesa, mage, equip):
        self.atk = atk
        self.defesa = defesa
        self.mage = mage
        self.equip = equip

    def nivel(self):
        niveis = int(input('Qual seu nível?'))
        self.atk += (5 * niveis)
        self.defesa += (3 * niveis)
        ataque = self.atk
        defesaheroi = self.defesa
        print(f'Seu ataque é de {ataque} pontos e sua defesa é {defesaheroi} pontos.')
        
    def equipamento(self):
        equips = str(input('Escolha seu equipamento: Espada, Machado ou Arco?')).lower().replace(' ' , '')
        if equips == 'espada':
            self.atk += 20
        elif equips == 'machado':
            self.atk += 25
        elif equips == 'arco':
            self.atk += 20
        print(f'Seu ataque agora é de {self.atk}')

guerreiro1 = Guerreiro(1, 1, 0, 0)
guerreiro1.nivel()
guerreiro1.equipamento()
