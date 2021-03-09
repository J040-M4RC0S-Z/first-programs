print("\033[1;35mTriângulo type\033[m")

r1 = float(input("Digite a primeira medida do triângulo: "))
r2 = float(input("Digite a segunda medida do triângulo: "))
r3 = float(input("Digite a terceira medida do triângulo: "))

if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    if r1 == r2 and r2 == r3 and r3 == r1:
        print("Com essas medidas é possível formar um triângulo Equilátero.")
if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    if r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print("É possível formar um triângulo isóceles !")
if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    if r1 != r2 and r2 != r3 and r3 != r1:
        print("É possível formar um triângulo Escaleno")
else:
    print("Não é possível formar um triângulo com essas medidas de retas. ")

#Outro código

print("\033[1;36mClassificador de triângulos\033[m")
res = 'S'
while res == "S":
    r1 = int(input("Digite o tamnho da primeira reta: "))
    r2 = int(input("Digite o tamanho da segunda reta: "))
    r3 = int(input("Digite o tamanha da segunda reta: "))

    if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2) and r1 > (r2 - r3) and r2 > (r3 - r2) and r3 > (r2 - r3):
        print("Nessas condições podemos formar um triângulo e ele ", end="")
        if r1 == r2 == r3:
            print("será EQUILÁTERO !")
        elif r1 == r2 != r3 or r2 == r1 != r3 or r3 == r2 != r1 or r3 == r1 != r2 :
            print("será ISÓCELES !")
        elif r1 != r2 != r3 != r1:
            print("será ESCALENO ! ")
    else:
        print("Nessas condições não podemos ter um triângulo !")
    res = str(input("Você deseja fazer outro teste ? [S/N]")).strip().capitalize()[0]
print("Fim")