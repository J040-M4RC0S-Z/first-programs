from random import randint
escolha_computador = randint(0, 10)
print("-=-"*30)
print("O Computador escolheu um número de 0 a 10, será que você consegue adivinhar qual é ?")
num = int(input("Digite um palpite entre 0 e 10: "))
print("-=-"*30)
cont = 1
while num != escolha_computador:
    print("Hmmm... Você errou :(")
    if num < escolha_computador:
        print("Dica: Chute um número maior !")
    if num > escolha_computador: 
        print("Dica: Chute um número menor !")
    num = int(input("Dê outro palpite: "))
    print("-=-"*10)
    cont += 1 
print(f"Parabéns ! Você acertou com {cont} tentativas !")
print(f"Número escolhido pelo computador: {escolha_computador}")