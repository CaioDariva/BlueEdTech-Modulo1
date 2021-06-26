# Crie um programa que simule um sistema de votação, ele deve receber votos até que o usuário diga que não tem 
# mais ninguém para votar, esse programa precisa ter duas funções: 

# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o ano de nascimento de uma 
# pessoa que será digitado pelo usuário, retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL e OBRIGATÓRIO nas eleições. 

# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá da função 
# autoriza_voto()) e o voto que é o número que a pessoa votou. 
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o contrário a 2° função 
# deve validar o número que a pessoa escolheu, ela pode escolher de 1 a 5 (crie 3 candidatos para a votação): 
# 1, 2 ou 3 - Votos para os respectivos candidatos  
# 4- Voto Nulo 
# 5 - Voto em Branco 

# Sua função votacao() tem que calcular e mostrar: 
# O total de votos para cada candidato; 
# O total de votos nulos; 
# O total de votos em branco; 
# Qual candidato venceu a votação. 

def autoriza_votos(nascimento):
        if nascimento > 2005:
            return 'NEGADO' 
        elif nascimento == 2004 or nascimento == 2005:
            return 'OPCIONAL'
        elif nascimento < 1951:
            return 'OPCIONAL'
        else:
            return 'OBRIGATÓRIO'

def votacao(autorizacao, voto):    
    if autorizacao == 'NEGADO':
        print('Você não pode votar')
    if autorizacao == 'OBRIGATÓRIO' or autorizacao == 'OPCIONAL':
        return 'Voto Validado'

jose = 0
joao = 0
jamily = 0
nulo = 0
branco = 0

continuar = 'sim'
while continuar == 'sim':
    print('Vamos votar!')
    print()
    ano = int(input('Primeiro precisamos saber em que ano você nasceu?\n'))
    voto = int(input('Agora escolha o seu voto!\nDigite 1 para João.\nDigite 2 para José.\nDigite 3 para Jandira.\nDigite 4 para anular seu voto.\nDigite 5 para votar em branco.\n'))
    while voto > 5 or voto < 1:
        voto = int(input('Inválido!\nDigite 1 para João.\nDigite 2 para José.\nDigite 3 para Jandira.\nDigite 4 para anular seu voto.\nDigite 5 para votar em branco.\n'))
    validacao = votacao(autoriza_votos(ano), voto)
    if validacao == 'Voto Validado' and voto == 1:
        joao += 1
    elif validacao == 'Voto Validado' and voto == 2:
        jose += 1
    elif validacao == 'Voto Validado' and voto == 3:
        jamily += 1
    elif validacao == 'Voto Validado' and voto == 4:
        nulo += 1
    elif validacao == 'Voto Validado' and voto == 5:
        branco += 1
    continuar = str(input('Ainda tem mais eleitores para votar depois de você?')).lower().replace(' ','').replace('ã' , 'a')

if jose > joao and jose > jamily:
    print(f'João obteve {joao} votos, José obteve {jose} votos e Jandira obteve {jamily} votos.\nO total de votos nulos foi: {nulo}.\nO total de votos em branco foi: {branco}.\nJosé venceu as eleições!')
elif joao > jose and jose > jamily:
    print(f'João obteve {joao} votos, José obteve {jose} votos e Jandira obteve {jamily} votos.\nO total de votos nulos foi: {nulo}.\nO total de votos em branco foi: {branco}.\nJoão venceu as eleições!')
elif jamily > jose and joao:
    print(f'João obteve {joao} votos, José obteve {jose} votos e Jandira obteve {jamily} votos.\nO total de votos nulos foi: {nulo}.\nO total de votos em branco foi: {branco}.\nJandira venceu as eleições!')
