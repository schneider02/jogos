import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Definir largura e altura da tela
largura = 640
altura = 480

# Carregar som de colisão
barulho_colisao = pygame.mixer.Sound('8d82b5_SMW_Kick_Sound_Effect.wav')

# Definir posição inicial do jogador
x = int(largura/2)
y = int(altura/2)

# Definir posição inicial do retângulo azul
x_azul = randint(40, 600)
y_azul = randint(50, 430)

# Definir pontos e fonte para exibir na tela
pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

# Configuração da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

# Ajuste de volume e música de fundo
pygame.mixer.music.set_volume(0.07)
pygame.mixer.music.load('8bit-music-for-game-68698.mp3')  # Certifique-se de que o caminho está correto
pygame.mixer.music.play(-1)  # Loop infinito para a música

while True:
    relogio.tick(30)  # Controla o FPS (frames por segundo)
    tela.fill((0, 0, 0))  # Preenche a tela com a cor preta

    # Exibir a pontuação na tela
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    
    # Processar eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[K_a]:
        x -= 20
    if teclas[K_d]:
        x += 20
    if teclas[K_w]:
        y -= 20
    if teclas[K_s]:
        y += 20

    # Desenho do retângulo vermelho (jogador) e azul (inimigo)
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    # Verificar colisão
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        barulho_colisao.play()  # Tocar o som da colisão

    # Exibir a pontuação na tela
    tela.blit(texto_formatado, (400, 40))

    # Atualizar a tela
    pygame.display.update()
