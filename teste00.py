import pygame
from pygame.locals import * 
from sys import exit
from random import randint

pygame.init()

# Definir o tamanho da tela
largura = 640
altura = 480

# Som da colisão
barulho_colisao = pygame.mixer.Sound('smw_kick.wav')

# Posição inicial do jogador
x = int(largura / 2)
y = int(altura / 2)

# Posição do objetivo azul
x_azul = randint(40, 600)
y_azul = randint(50, 430)

# Variáveis de pontuação e fonte
pontos = 0 
fonte = pygame.font.SysFont('arial', 40, True, True)

# Configurar a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

# Música de fundo
pygame.mixer.music.set_volume(0.07)
musica_de_fundo = pygame.mixer.music.load('8bit-music-for-game-68698.mp3')
pygame.mixer.music.play(-1)

# Loop principal do jogo
while True:
    relogio.tick(30)  # Define o FPS
    tela.fill((173, 216, 230))  # Cor de fundo azul claro

    # Exibe a pontuação
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    # Verifica os eventos (exemplo de quit)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Controle de movimentação
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20

    # Limitar o movimento para que o jogador não saia da tela
    if x < 0:
        x = 0
    if x > largura - 40:
        x = largura - 40
    if y < 0:
        y = 0
    if y > altura - 50:
        y = altura - 50

    # Desenha os retângulos (jogador e objetivo)
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    # Verifica colisão e atualiza a pontuação
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        barulho_colisao.play()

    # Exibe a pontuação na tela
    tela.blit(texto_formatado, (10, 10))  # Ajuste a posição da pontuação

    # Atualiza a tela
    pygame.display.update()
