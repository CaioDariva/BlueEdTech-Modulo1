# As empresas @.com resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para 
# desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador 
# e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R 280,00eR  700,00 : aumento de 15%
# salários entre R 700,00eR  1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento."

reaj1 = 0.2
reaj2 = 0.15
reaj3 = 0.1
reaj4 = 0.05

salario = str(input("Qual é o seu salário?")).replace(',' , '.').replace(' ' , '')
salariocorreto = float(salario)

aumento1 = salariocorreto * reaj1
aumento2 = salariocorreto * reaj2
aumento3 = salariocorreto * reaj3
aumento4 = salariocorreto * reaj4

print(f'O seu salário atual é: R$ {salariocorreto:.2f}.')

if salariocorreto <= 280:
  print(f'O seu salário irá aumentar {reaj1 * 100}%.')
  print(f'Portanto, o seu salário irá aumentar R$ {salariocorreto * reaj1:.2f}.')
  print(f'E seu salário total será de R$ {salariocorreto + aumento1:.2f}.')
elif salariocorreto > 280 and salariocorreto < 700:
  print(f'O seu salário irá aumentar {reaj2 * 100}%')
  print(f'Portanto, o seu salário irá aumentar R$ {salariocorreto * reaj2:.2f}.')
  print(f'E seu salário total será de R$ {salariocorreto + aumento2:.2f}.')
elif salariocorreto >= 700 and salariocorreto < 1500:
  print(f'O seu salário irá aumentar {reaj3 * 100}%')
  print(f'Portanto, o seu salário irá aumentar R$ {salariocorreto * reaj3:.2f}.')
  print(f'E seu salário total será de R$ {salariocorreto + aumento3:.2f}.')
elif salariocorreto >= 1500:
  print(f'O seu salário irá aumentar {reaj4 * 100}%')
  print(f'Portanto, o seu salário irá aumentar R$ {salariocorreto * reaj4:.2f}.')
  print(f'E seu salário total será de R$ {salariocorreto + aumento4:.2f}.')