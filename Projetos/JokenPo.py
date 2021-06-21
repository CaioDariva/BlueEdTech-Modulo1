## Utilizando os conceitos aprendidos até estruturas de repetição, crie um programa que jogue pedra, 
# papel e tesoura (Jokenpô) com você.  
## O programa tem que:  
## • Permitir que eu decida quantas rodadas iremos fazer; 
## • Ler a minha escolha (Pedra, papel ou tesoura); 
## • Decidir de forma aleatória a decisão do computador;
## • Mostrar quantas rodadas cada jogador ganhou; 
## • Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um 
## (computador e jogador); 
## • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade de rodadas, 
## se não finalize o programa. 

import random

continuacao = 'SIM'

while continuacao == 'SIM':
    jogos = 1
    empate = 0
    num_vitorias_jog = 0
    num_vitorias_comp = 0

    num_jogos = int(input('Vamos jogar Jokempô! Quantas rodadas iremos jogar?\n'))

    while num_jogos >= jogos:
        jogador = input('Ok! Vamos lá!\nJo - Kem - Pô?\n').upper()
        print()
        comp = random.randint(1,3)
        if comp == 1:
            comp = 'PEDRA'
        elif comp == 2:  
            comp = 'PAPEL'
        elif comp == 3:
            comp = 'TESOURA'
        print(f'Você tirou {jogador} e o computador tirou {comp}!')
        print()
        if jogador == comp:
            print('Empatou!')
            empate += 1
        elif jogador == 'TESOURA' and comp == 'PAPEL':
            print('Você ganhou!')
            num_vitorias_jog += 1
        elif jogador == 'TESOURA' and comp == 'PEDRA':
            print('Você perdeu!')
            num_vitorias_comp += 1
        elif jogador == 'PAPEL' and comp == 'PEDRA':
            print('Você ganhou!')
            num_vitorias_jog += 1
        elif jogador == 'PAPEL' and comp == 'TESOURA':    
            print('Você perdeu!')
            num_vitorias_comp += 1
        elif jogador == 'PEDRA' and comp == 'TESOURA':
            print('Você ganhou!')
            num_vitorias_jog += 1
        elif jogador == 'PEDRA' and comp == 'PAPEL':    
            print('Você perdeu!')
            num_vitorias_comp += 1
        jogos += 1

    print()

    print(f'Você ganhou {num_vitorias_jog}x.\nO computador {num_vitorias_comp}x.\nEmpatou {empate}x.')

    print()

    if num_vitorias_jog > num_vitorias_comp:
        print('Parabéns! Você é o rei do Jokempô!')
    elif num_vitorias_jog == num_vitorias_comp:
        print('Houve um empate aqui!')
    elif num_vitorias_jog < num_vitorias_comp:
        print('Você perdeu, que pena!')

    print()

    continuacao = input('Deseja jogar novamente?').upper().replace('Ã' , 'A')

print()

if continuacao == 'NAO':
    print('O jogo terminou. Espero que tenha se divertido!\n')