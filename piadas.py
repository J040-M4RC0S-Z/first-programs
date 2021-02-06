import time
print("Escolha um número de 1 até 10 e receba uma piada: ")
resposta = "S"
while resposta == "S":
    num = int(input("Digite um número: "))

    if num == 1:
        print("""Patinhos
          O que o pato disse para a pata? 
          "R.: Vem Quá!""")
    if num == 2:
        print("""Alô?
          Porque o menino estava falando no telefone deitado?
          R.: Para não cair a ligação;""")
    if num == 3:
        print("""Paciente sumidinho... 
          A enfermeira diz ao médico:
          – Tem um homem invisível na sala de espera.
          O médico responde:
          – Diga a ele que não posso vê-lo agora.""")
    if num == 4:
        print("""Amém
            Qual é a fórmula da água benta?
            R.: H Deus O!""")
    if num == 5:
        print("""Fumiga
            "Duas formigas japonesas se encontraram e pararam para conversar:
            - Oi, qual seu nome?"
            - Fu."         - Fu o que?
            - Fu Miga!""")
    if num == 6:
        print("""O pintinho e a mãe
            O que o pintinho falou para a mãe dele?
            R.: Oi mãe!""")
    if num == 7:
        print("""Fujão!
        No zoológico, um canguru vivia fugindo do cercado. 
        Os tratadores sabiam que ele pulava alto e construíram uma cerca de 3 metros.
        Não adiantou, porque o canguru sempre fugia. 
        Então, ergueram uma cerca de 6 metros. E ele saiu de novo.
        Quando a cerca já estava com 12 metros, o camelo do cercado vizinho perguntou ao canguru:
        – Até que altura você acha que eles vão?
        O canguru respondeu:
        – Mais de 300, a menos que alguém tranque o portão à noite.""")
    if num == 8:
        print("""Trollei!
        Na manhã de seu aniversário, uma mulher disse ao marido:
        - Sonhei que você me dava um colar de diamantes. O que acha que isso significa?
        - Talvez você descubra hoje à noite - respondeu ele.
        Naquela noite, o homem chegou em casa com um pequeno pacote e o entregou à mulher. 
        Ela rasgou o papel de embrulho, ansiosa, e encontrou um livro: O significado dos sonhos.""")

    if num == 9:
        print("""Acorda aí
            O diretor da empresa pergunta ao novo funcionário:
            – O    contador já lhe disse qual é sua tarefa?
        – Sim. Acordá-lo quando eu perceber que o senhor está vindo.""")
    if num == 10:
        print("""Alô Deus?!
            O condenado à morte esperava a hora da execução, quando chegou o padre:
            - Meu filho, vim trazer a palavra de Deus para você.
            - Perda de tempo, seu padre. Daqui a pouco vou falar com Ele, pessoalmente. Algum recado?""")
    elif num > 10:
        print("Caregando...")
        time.sleep(3/2)
        print("Não Temos nenhuma piada com essa opção :(.")
    resposta = input("Deseja continuar ? [S/N]").upper().strip()[0]
else:
    time.sleep(3/2)
    print("Fim")
