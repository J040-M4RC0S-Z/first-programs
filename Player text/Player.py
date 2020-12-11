import pygame

change = int(input('Digite o Número da música que você deseja tocar: [1/2/3/4]: '))

if change == (1000-999):
    print("Está tocando: 'Diego e Vitor Hugo - Pisadinha'")
    music1= pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('pis.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    input()

elif change == (100/50):
    print("Está tocando: 'HUNGRIA - Amor e fé'")
    music2 = pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('aef.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    input()

elif change == (4860/1620):
    print("Está tocando: 'Ilusão - Cracolândia' ")
    music3 = pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('ccl.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    input()

elif change == 4:
    print("Está tocando: 'Samahnta - Nave Espacial'")
    music4 = pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('nep.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    input()
else:
    print('None')




