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
r_largura = 100
r_altura = 50
r_x = largura // 2 - r_largura // 2
r_y = altura // 2 - r_altura // 2

#angulo de rotação em graus
angulo = 0

#velocidade de rotação
r_velocidade = 2

#função para desenhar o retângulo rotacionado
def retangulo_rotate(canvas, cor, x, y, largura, altura, angulo):
    ret_rotate = pygame.Surface((altura, largura), pygame.SRCALPHA)
    ret_rotate.fill((0, 0, 0, 0))
    pygame.draw.rect(ret_rotate, cor, (0, 0, largura, altura))
    rotacao = pygame.transform.rotate(ret_rotate, angulo)
    novo_retangulo = rotacao.get_rect(center = (x, y))
    canvas.blit(rotacao, novo_retangulo.topleft)

    #loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0) #sair da aplicação
    #limpar a tela
    tela.fill((0,0,0,0))

    #desenhar o retangulo rotacionado
    retangulo_rotate(tela, vermelho, r_x, r_y, r_largura, r_altura, angulo)

    #atualizar a tela
    pygame.display.flip()

    #realizar a rotação
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_LEFT]:
        angulo -= r_velocidade
    if tecla[pygame.K_RIGHT]:
        angulo += r_velocidade
    
    #atualizar tela
    pygame.display.update()
pygame.quit()
