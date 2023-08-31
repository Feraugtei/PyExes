import pygame
import sys
import math
pygame.init ()

#configuração de janela
altura, largura = 800, 600
tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption("Rotação")

#cores
cinza = (100, 100, 100)
vermelho = (255, 0, 0)

#variaveis do retangulo
r_largura = 300
r_altura = 100
r_x = largura // 2 - r_largura // 2
r_y = altura // 2 - r_altura // 2

#fator de escala
escala = 1.0

#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0) #sair da aplicação
    #limpar a tela
    tela.fill((0,0,0,0))

    #desenhar o retangulo
    r_largura = int(largura * escala)
    r_altura = int (altura * escala)
    pygame.draw.rect(tela, vermelho, (r_x, r_y, r_largura, r_altura))

    #atualizar a tela
    pygame.display.flip()

    #realizar a rotação
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP]:
        escala += 0.005
    if tecla[pygame.K_DOWN]:
        escala -= 0.005

    #limitar a escala
    escala = max(0.01, escala)

    pygame.display.update
    
pygame.quit()
