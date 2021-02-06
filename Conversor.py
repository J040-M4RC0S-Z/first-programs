print("""Escolha uma opção para fazer a conversão: 
        [1] °C => °F
        [2] °F => °C
        [3] °C => °K
        [4] °K => °C
        [5] °F => °K 
        [6] °K => °F
""")
resposta = "S"
while resposta == "S":
        opcao = int(input("Digite a opção escolhida: "))
        if opcao == 1:
            celsius = float(input("Digite quantos graus voce deseja converter: "))
            operação = ((celsius * 5)/9 + 32)
            print(f"{celsius}°C ficará {operação:.2f}°F")
        if opcao == 2:
            farenheint = float(input("Digite um quantos graus você deseja converter: "))
            operação = (farenheint - 32)/1.8
            print(f"{farenheint}°F ficará {operação:.2f}°C")
        if opcao == 3:
            celsius = float(input("Digite quantos graus você deseja converter: "))
            operação = celsius + 273.15
            print(f"{celsius}ºC ficará {operação:.2f}ºK")
        if opcao == 4:
            kelvin = float(input("Digite quantos graus você deseja converter: "))
            operação = kelvin - 273.15
            print(f"{kelvin}°K ficará {operação:.2f}°C")
        if opcao == 5:
             farenheint = float(input("Digite quantos graus você deseja converter: "))
             operação = ((farenheint - 32) * (5/9)) + 273.15
             print(f"{farenheint}°F ficará {operação:.2f}°K.")
        if opcao == 6:
            kelvin = float(input("Digite quantos graus você deseja converter: "))
            operação = ((kelvin - 273.15) * (9/5) + 32)
            print(f"{kelvin}°K ficará {operação:.2f}°F")
        elif opcao > 6 or opcao < 1:
            print("ERROR 1")
        resposta = input( "Deseja continuar ? [S/N]").upper().strip()[0]
print("Fim")