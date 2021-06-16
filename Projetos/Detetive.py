# Agora com While para não ter como o usuário dar entrada incorreta
# Projeto 01 – Detetive - Esse projeto tem a finalidade de fixar os conhecimentos de Variáveis, Print, Input e Condicionais, para isso crie um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# • "Você telefonou para a vítima?"
# • " Você esteve no local do crime?"
# • " Você mora perto da vítima?"
# • " Você devia para a vítima?"
# • " Você já trabalhou com a vítima?"
# O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a:
# • 2 questões ela deve ser classificada como "Suspeita",
# • Entre 3 e 4 como "Cúmplice"
# • 5 como "Assassino".
# • Caso contrário, ele será classificado como "Inocente".

perg1 = str(input('Você telefonou para a vítima? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')
while perg1 != 'SIM' and perg1 != 'NAO':
  perg1 = str(input('Você telefonou para a vítima? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')
perg2 = str(input('Você esteve no local do crime? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')
while perg2 != 'SIM' and perg2 != 'NAO':
  perg2 = str(input('Você esteve no local do crime? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')
perg3 = str(input('Você mora perto da vítima? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')
while perg3 != 'SIM' and perg3 != 'NAO':
  perg3 = str(input('Você mora perto da vítima? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')
perg4 = str(input('Você devia para a vítima? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')
while perg4 != 'SIM' and perg4 != 'NAO':
  perg4 = str(input('Você devia para a vítima? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')
perg5 = str(input('Você já trabalhou com a vítima? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')
while perg5 != 'SIM' and perg5 != 'NAO':
  perg5 = str(input('Você já trabalhou com a vítima? Responda sim ou não: \n')).replace(' ' , '').upper().replace('Ã' , 'A')

var1 = (perg1).replace('SIM' , '1'). replace('NAO' , '2')
r1 = int(var1)
var2 = (perg2).replace('SIM' , '1'). replace('NAO' , '2')
r2 = int(var2)
var3 = (perg3).replace('SIM' , '1'). replace('NAO' , '2')
r3 = int(var3)
var4 = (perg4).replace('SIM' , '1'). replace('NAO' , '2')
r4 = int(var4)
var5 = (perg5).replace('SIM' , '1'). replace('NAO' , '2')
r5 = int(var5)

resposta = int(r1 + r2 + r3 + r4 + r5)

if resposta == 5:
  print('Você é o Assassino!')
elif (resposta == 6) or (resposta == 7):
  print('Você é: Cúmplice!')
elif resposta == 8:
  print('Você é: Suspeito!')
elif (resposta == 9) or (resposta == 10):
  print('Você é: Inocente!')