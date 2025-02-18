import pygame
from pygame.locals import * 
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
     
tela = pygame.display.set_mode((largura, altura))  # Corrigido para tupla

# musica_de_fundo = pygame.mixer.music.load('8bit-music-for-game-68698.mp3')
# pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # Corrigido para QUIT em maiúsculas
            pygame.quit()
            exit()
    
    pygame.display.update()
