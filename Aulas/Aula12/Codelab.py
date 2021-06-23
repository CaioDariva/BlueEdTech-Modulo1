# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 
# 5 e 6.9 está de recuperação, caso contrário é reprovado.

dicionario = {}
nota = []
nome = input('Qual é o seu nome?\n')

for i in range(3):
    notas = float(input('Qual foi a sua nota?:\n'))
    nota.append(notas)
soma=sum(nota)
media= soma/3
if media > 5 and media <= 6.9:
    print(f'Você esta em recuperação, sua media foi de {media:.2f}')
elif media >= 7:
    print(f'Parabens você foi aprovado!!! sua media foi de {media:.2f}')
else:
    print(f'Você foi reprovado =( sua media foi de {media:.2f}')

dicionario[nome] = nota
print(dicionario)




# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um 
# dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o 
# salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o 
# trabalhador deve contribuir por 35 anos para se aposentar.​​

dicionario = {}
continucao = 0
while continucao != 'Não':
    nome = input('Qual é o seu nome? \n')
    nascimento = int(input('Em que ano você nasceu?:\n'))
    carteira = int(input('Digite os numeros da sua carteira de trabalho:\n'))
    idade = 2021 - nascimento
    dicionario[nome] = nascimento, idade
    if carteira != 0:
        contratacao = int(input('Em que ano você começou a trabalhar?\n'))
        salario = float(input('Qual é o seu salario?\n R$'))
        aposentar = (contratacao + 35) - nascimento
        dicionario[nome] = nascimento, idade, salario, aposentar

    continucao = input('Deseja cadastrar outra pessoa?\n').capitalize().replace(' ','').replace('a','ã')

print(dicionario)






# 3.	DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão 
# 2.	Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário 
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , 
# com quantos anos a pessoa vai se aposentar.
#  Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

lista = []
nome = 0
sexo = 0
idades = []
pessoas = 0
quantidade_F =[]
idade_acima_media = []
media_idade=[]
cadastro=0
while cadastro != 'Não':
    pessoas +=1
    dicionario = {}
    nome=input('Qual é o seu nome?\n').title().strip()
    sexo=input('Qual é o seu sexo? Masculino ou Feminino:\n').capitalize().strip()
    while sexo != 'Masculino' and sexo != 'Feminino':
        sexo=input('Qual é o seu sexo? Masculino ou Feminino:\n').capitalize().strip()
    if sexo == 'Feminino':
        quantidade_F.append(nome)
    idade=int(input('Qual é a sua idade?\n'))
    cadastro = input('Deseja cadastrar outra pessoa?:\n').capitalize().replace('a','ã').replace(' ','')
    dicionario[nome] = sexo, idade
    idades.append(idade)
    lista.append(dicionario)
soma_idade=sum(idades)
media_idade= soma_idade/pessoas
for i in idades:
    if i > media_idade:
        idade_acima_media.append(i)

print()
print(f'Minha lista {lista}')
print()
print(f'As mulheres são {quantidade_F}')
print()
print(f'{idade_acima_media}São as idades que estão acima da media')
print()
print(f'A media de idades é de {media_idade}')





# Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve receber 5 notas de 
# 15 alunos, assim como o nome desses alunos, o programa tem que calcular a média desse aluno e mostrar a 
# situação dele, seguindo os mesmos critérios apresentados no exercício 3. No final apresente todos nomes, 
# as 5 notas, as médias e as situações dos 15 alunos de uma vez só.

alunos = {}
for i in range(2):
    nome=input('Qual é o seu nome?\n')
    lista_notas=[]
    soma=0
    for u in range(5):
        nota=float(input('Digite a sua nota:\n'))
        lista_notas.append(nota)
        soma=sum(lista_notas)
        media=soma/5
    situacao= 0
    if media > 5 and media <= 6.9:
        situacao='Recuparação'
    elif media >= 7:
        situacao='Aprovado'
    else:
        situacao='Reprovado'
    alunos[nome]= lista_notas, media,situacao
print(alunos)

#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. 
# No final tudo isso será guardado em um dicionário, incluindo a média de gols por jogo, e o total 
# de gols feitos durante o campeonato.
