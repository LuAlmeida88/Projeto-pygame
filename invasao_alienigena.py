import sys
import pygame

def iniciar_jogo():
    # Inicializa  o jogo e cria um objeto para a tela
    pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Invasão Alienigena")

# Inicia o laço principal do jogo
while True:
    #Observa os elementos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

                #Deixa a tela mais recente visivel 
                pygame.display.flip()
iniciar_jogo()