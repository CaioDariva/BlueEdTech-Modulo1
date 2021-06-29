def autoriza_voto(ano):
    if ano > 2005:
        print('O eleitor não está apto a votar!')
        print()
    elif ano == 2005 or ano == 2004:
        print('O voto é Opcional!')
        print()
        return 'ok'
    elif ano < 1951:
        print('O voto é Opcional!')
        print()
        return 'ok'
    elif ano >= 1951 and ano < 2004:
        print('O voto é Obrigatório!')
        print()
        return 'ok'

candidato1 = []
candidato2 = []
candidato3 = []
nulo = []
branco = []

def votacao(validade, voto):
    if cont == 'sim':
        if validade == 'ok':
            pass
        if voto == 1:
            candidato1.append(1)
        elif voto == 2:
            candidato2.append(1)
        elif voto == 3:
            candidato3.append(1)
        elif voto == 4:
            nulo.append(1)
        elif voto == 5:
            branco.append(1)
    else:
        print(f'O candidato 1 teve {sum(candidato1)} voto(s).\nO candidato 2 teve {sum(candidato2)} voto(s).\nO candidato 3 teve {sum(candidato3)} voto(s).\n{sum(nulo)} voto(s) nulo(s).\n{sum(branco)} voto(s) em branco.')
        if sum(candidato1) > sum(candidato2) and sum(candidato1) > sum(candidato3):
            print('O candidato 1 venceu as eleições.')
        elif sum(candidato2) > sum(candidato3) and sum(candidato2) > sum(candidato1):
            print('O candidato 2 venceu as eleições.')
        elif sum(candidato3) > sum(candidato2) and sum(candidato3) > sum(candidato1):
            print('O candidato 3 venceu as eleições.')
        elif sum(candidato1) == sum(candidato2) and sum(candidato2) == sum(candidato3):
            print('Houve um empate triplo.')
        elif sum(candidato1) == sum(candidato2) and sum(candidato2) != sum(candidato3):
            print('Houve um empate entre os candidatos 1 e 2.')
        elif sum(candidato1) == sum(candidato3) and sum(candidato3) != sum(candidato2):
            print('Houve um empate entre os candidatos 1 e 3.')
        elif sum(candidato2) == sum(candidato3) and sum(candidato3) != sum(candidato1):
            print('Houve um empate entre os candidatos 2 e 3.')
            
cont = 'sim'
print('---'*4, 'Vamos Votar', '---'*4)
while cont == 'sim':
    anoNascimento = int(input('Qual é o ano de nascimento do eleitor?\n'))
    print()
    if autoriza_voto(anoNascimento) == 'ok':
        validade = 'ok'
        voto = int(input('Vote 1 para Candidato 1.\nVote 2 para Candidato 2.\nVote 3 para Candidato 3.\nVote 4 para voto Nulo.\nVote 5 para voto em Branco.\nQual será o seu voto?\n'))
        while voto != 1 and voto != 2 and voto != 3 and voto != 4 and voto != 5:
            print('Inválido.')
            print()
            voto = int(input('Vote 1 para Candidato 1.\nVote 2 para Candidato 2.\nVote 3 para Candidato 3.\nVote 4 para voto Nulo.\nVote 5 para voto em Branco.\nQual será o seu voto?\n'))
        print()
        votacao(validade, voto)
    cont = str(input('Existem mais pessoas para votar?\n')).lower().replace('ã' , 'a').replace(' ' , '')
    while cont != 'sim' and cont != 'nao':
        cont = str(input('Por favor, responda com "sim" ou "não". Existem mais pessoas para votar?\n')).lower().replace('ã' , 'a').replace(' ' , '')
    print()

votacao(validade, voto)