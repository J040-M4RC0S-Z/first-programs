import time
import random
print("Pedra, Papel, Tesoura:")
print("""\033[1;35mSuas Opões\033[m:
         \033[36m[0] PEDRA\033[m
         \033[37m[1] PAPEL\033[m
         \033[33m[2] TESOURA\033[m""")
vitorias = 0
res = "S"
while res == "S":
    opcao_jogador = int(input("Digite a sua opção: "))
    opcoes = ["PEDRA","PAPEL","TESOURA"]
    opcao_computador = (random.choice(opcoes))

    print(opcao_computador)
    print("- JO -")
    time.sleep(3/10)
    print("= KEN =")
    time.sleep(3/10)
    print("=- PÔ ! -=")
    print("-="*10)
    if opcao_jogador == 0 and opcao_computador == "PEDRA":
        print(f"EMPATE ! ESCOLHA JOGADOR: PEDRA \n"
          f" COM: {opcao_computador}")
    elif opcao_jogador == 1 and opcao_computador == "PAPEL":
        print(f"EMPATE ! \n Sua Escolha: PAPEL \n Escolha do COM: {opcao_computador}")
    elif opcao_jogador == 2 and opcao_computador == "TESOURA":
        print(f"EMPATE \n Sua escolha: Tesoura \n Escolha do COM: {opcao_computador}")
    elif opcao_jogador == 0 and opcao_computador == "PAPEL":
        print(f"VOCÊ PERDEU ! :( \n Sua escolha: PEDRA \n Escolha COM: {opcao_computador}")
    elif opcao_jogador == 0 and opcao_computador == "TESOURA":
        print(f"VOCÊ GANHOU ! :) \n Sua escolha: PEDRA \n Escolha COM: {opcao_computador}")
        vitorias += 1
    elif opcao_jogador == 1 and opcao_computador == "PEDRA":
        print(f"VOCÊ GANHOU !:) \n Sua escolha: PAPEL \n Escolha COM: {opcao_computador}")
        vitorias += 1
    elif opcao_jogador == 1 and opcao_computador == "TESOURA":
        print(f"VOCÊ PERDEU ! :( \n Sua escolhha: PAPEL \n Escolha COM: {opcao_computador}")
    elif opcao_jogador == 2 and opcao_computador =="PEDRA":
        print(f"VOCÊ PERDEU ! :( \n Sua escolha: TESOURA \n Escolha COM: {opcao_computador}")
    elif opcao_jogador == 2 and opcao_computador == "PAPEL":
        print(f"VOCÊ GANHOU ! :) \n Sua escolha: TESOURA \n Escolha COM: {opcao_computador}")
        vitorias += 1
    else:
        print("opção não encontrada")
    res = input("Deseja jogar outra vez? [S/N]").strip().capitalize()[0]
print(f"Você conseguiu vencer {vitorias} vezes ! PARABÉNS !")
print("-="*10)
