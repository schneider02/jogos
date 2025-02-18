import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

barulho_colisao = pygame.mixer.Sound('8d82b5_SMW_Kick_Sound_Effect.mp3')

x = int(largura/2)
y = int(altura/2)

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0 
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

pygame.mixer.music.set_volume(0.50)
musica_de_fundo = pygame.mixer.music.load('8bit-music-for-game-68698.mp3')
pygame.mixer.music.play(-1)

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado  = fonte.render(mensagem, True, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            if event.key == K_d:
                x += 20
            if event.key == K_w:
                y -= 20
            if event.key == K_s:
                y += 20

    # Restricting the red rectangle inside the screen
    if x < 0: x = 0
    if x > largura - 40: x = largura - 40
    if y < 0: y = 0
    if y > altura - 50: y = altura - 50

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        barulho_colisao.play()

    tela.blit(texto_formatado, (400, 40))
    pygame.display.update()
