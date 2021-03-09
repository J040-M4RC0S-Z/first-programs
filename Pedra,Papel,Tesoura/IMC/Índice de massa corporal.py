import math
print("\033[1;35mIMC\033[m")
alt = float(input("Digite a sua altura (metros): "))
peso = float(input("Digite o seu peso (kilos): "))
imc = peso/math.pow(alt,2)

if imc < 18.5:
    print(f"""IMC: {imc:.2f}
          Situação: Abaixo do peso""")
elif 18.5 <= imc <= 25:
    print(f"""IMC: {imc:.2f}
          Situação: Peso Ideal""")
elif 25 <= imc <=30:
    print(f"""IMC: {imc:.2f}
          Situação: Sobrepeso""")
elif 30 <= imc <= 40:
    print(f"""IMC: {imc:.2f}
          Situação: Obesidade""")
elif imc > 40:
    print(f"""IMC: {imc:.2f}
          Situação: Obesidade Mórbida""")
else:
    print("opção não encontrada")