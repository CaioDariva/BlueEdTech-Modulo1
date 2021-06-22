#3- Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma 
# aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random

palavras = ['animal']

palavra_aleat = random.choice(palavras)
contadorletras = 0
tentativas = 6

letra_escolhida = str(input(f'Vamos jogar forca!\nA palavra possui {len(palavra_aleat)} letras.\nVocê tem {tentativas} tentativa(s). Digite uma letra:')).lower()


while tentativas > 0:
    for i, j in enumerate(palavra_aleat):
        if j == letra_escolhida:
            print(f'A letra "{j}" está na posição {i + 1}.')
            contadorletras += 1
    if contadorletras == len(palavra_aleat):
        break
    tentativas -= 1
    letra_escolhida = str(input('Digite a próxima letra: '))