altura = float(input("Qual é a sua altura?").replace("," , ".").strip().lower().replace("m" , ""))
peso = float(input("Qual é o seu peso?").replace("," , ".").strip().lower().replace("k" , "").replace("g" , ""))
imc = float(f"{peso / (altura * altura):.2f}")

if imc < 18.5:
  print(f"Seu IMC é de: {imc} e sua classificação é MAGREZA")
if imc < 24.9 and imc >= 18.5:
  print(f"Seu IMC é {imc} e sua     classificação é NORMAL")
if imc < 29.9 and imc >= 25:
  print(f"Seu IMC é {imc} e sua classificação é SOBREPESO")
if imc < 39.9 and imc >= 30:
  print(f"Seu IMC é {imc} e sua classificação    é OBESO")
if imc > 40:
  print(f"Seu IMC é {imc} e   sua classificação é OBESIDADE GRAVE, SE CUIDE!")
