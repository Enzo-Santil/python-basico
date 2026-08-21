def calcular_imc(peso, altura):
	return peso / (altura ** 2)

peso = float(input("Digite o peso (kg):"))
altura = float(input("Digite a altura (m):"))

imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:2f}")

if imc < 18.5:
	print("Classificação: Abaixo do peso")
elif imc < 25:
	print("Peso normal")
elif imc < 30:
	print("Sobrepeso")
else:
	print("Obesidade")