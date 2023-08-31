import pygame
import sys
pygame.init()

#configuracao da janela
janela = (800, 600)
tela = pygame.display.set_mode(janela)
pygame.display.set_caption("translacao")

#cores
branco = (255, 255, 255)
azul = (0, 0, 255)

#variaveis do circulo
raio = 50
circulo_x = 600 // 2
circulo_y = 800 // 2

#velocidade de translação
v_translacao = 5

#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0) #sair da aplicação
    #limpar a tela
    tela.fill(branco)

    #desenhar o circulo
    pygame.draw.circle(tela, azul, (circulo_x, circulo_y), raio)

    #atualizar tela
    pygame.display.flip()

    #translação
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_LEFT]:
        circulo_x -= v_translacao
    if tecla[pygame.K_RIGHT]:
        circulo_x += v_translacao
    if tecla[pygame.K_UP]:
        circulo_y -= v_translacao
    if tecla[pygame.K_DOWN]:
        circulo_y += v_translacao
    
    #limitar a posição do circulo
    circulo_x = max(raio, min(800-raio, circulo_x))
    circulo_y = max(raio, min(600-raio, circulo_y))
    pygame.display.update()
pygame.quit()