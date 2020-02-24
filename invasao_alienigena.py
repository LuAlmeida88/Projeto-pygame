import sys
import pygame
from pygame.locals import*

def iniciar_jogo():
    pygame.init()
#Define o tamanho da tela
tela = pygame.display.set_mode((1200, 800))
Clock = pygame.time.Clock()
continuar = True
#Inicia o laço do jogo
while(continuar):
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type ==QUIT:
            continuar = False
#Define a cor de fundo da tela pygame
    tela.fill((230, 230, 230))
    pygame.display.flip()
iniciar_jogo()