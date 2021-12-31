import pygame
from pygame.locals import *
from sys import exit
from PIL import ImageColor
from random import randint

pygame.init()

# Música de fundo
pygame.mixer.music.set_volume(0.7)
musica_de_fundo = pygame.mixer.music.load("85 Mining Melancholy.mp3")
pygame.mixer.music.play(-1)

# Som interação cobra/maçã
barulho_colisao = pygame.mixer.Sound("smw_jump.wav")
barulho_colisao.set_volume(1)

# Cores em código RGB
vermelho = ImageColor.getrgb("red")
amarelo = ImageColor.getrgb("yellow")
rosa = ImageColor.getrgb("pink")
preto = ImageColor.getrgb("black")
verde = ImageColor.getrgb("green")
branco = ImageColor.getrgb("white")

# Tamanho da tela
largura = 640
altura = 480

# Posição da cobra
x = largura / 2
y = altura / 2

x_controle = 10
y_controle = 0

# Posição da maçã
x_maca = randint(0, 630)
y_maca = randint(0, 470)

# velocidade da mudança de direção
velocidade = 4

# Taxa de atualização da tela
frame = 60

# Pontuação inicial
pontos = 0

# Definindo fonte das letras
fonte = pygame.font.SysFont("arial", 30, True, True)

# Configuração do display
tela = pygame.display.set_mode((largura, altura))

# Definindo display do jogo
pygame.display.set_caption("Jogo")

# Definindo um relógio que faz a atualização dos frames
relogio = pygame.time.Clock()

#lista com valores da posição da cobra e seu tamanho inicial
lista_cobra = []
comprimento_inicial = 5

# Status da cobra
morreu = False

# Função que aumenta a cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, verde, (XeY[0], XeY[1], 10, 10))


# Função que reinicia o jogo com os valores iniciais
def reiniciar_jogo():
    global pontos, comprimento_inicial, x, y, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x = largura / 2
    y = altura / 2
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(0, 630)
    y_maca = randint(0, 470)
    morreu = False


while True:

    relogio.tick(frame)
    tela.fill(branco)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, amarelo)

    # Reconhece o os botões pressionados
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0


    # Atualiza o deslocamento da cobra
    x += x_controle
    y += y_controle

    # Desenha cobra na tela
    cobra = pygame.draw.rect(tela, verde, (x, y, 10, 10))
    # Desenha maçã na tela
    maca = pygame.draw.rect(tela, vermelho, (x_maca, y_maca, 10, 10))
    # Desenhando paredes
    parede_left_up = pygame.draw.rect(tela, rosa, (150, 120, 10, 100))
    parede_left_down = pygame.draw.rect(tela, rosa, (150, 260, 10, 100))
    parede_right_up = pygame.draw.rect(tela, rosa, (470, 120, 10, 100))
    parede_right_down = pygame.draw.rect(tela, rosa, (470, 260, 10, 100))
    parede_up = pygame.draw.rect(tela, rosa, (160, 120, 310, 10))
    parede_down = pygame.draw.rect(tela, rosa, (160, 350, 310, 10))

    paredes = [parede_up, parede_down, parede_right_up, parede_right_down, parede_left_up, parede_left_down]

    # Verifica colisão cobra/parede
    for parede in paredes:
        if cobra.colliderect(parede):
            fonte2 = pygame.font.SysFont("arial", 20, True, True)
            menssagem = "Game over, pressione R para reiniciar jogo!"
            texto_formatado = fonte2.render(menssagem, True, amarelo)
            ret_texto = texto_formatado.get_rect()

            morreu = True
            while morreu:
                tela.fill(branco)
                for event in pygame.event.get():
                    if event == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            reiniciar_jogo()

                ret_texto.center = (largura//2, altura//2)
                tela.blit(texto_formatado, ret_texto)
                pygame.display.update()


    # Verifica se a cobra encostou na maçã
    if cobra.colliderect(maca):
        x_maca = randint(0, 620)
        y_maca = randint(0, 460)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial += 1

    # Proibir a maçã de ser gerada nas paredes
    for parede in paredes:
        if cobra.colliderect(parede):
            x_maca = randint(0, 630)
            y_maca = randint(0, 470)


    lista_cabeca = []
    lista_cabeca.append(x)
    lista_cabeca.append(y)
    lista_cobra.append(lista_cabeca)

    # Condição para verificar se a cabeça da cobra encostou em seu corpo
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont("arial", 20, True, True)
        menssagem = "Game over, pressione R para reiniciar jogo!"
        texto_formatado = fonte2.render(menssagem, True, amarelo)
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill(branco)
            for event in pygame.event.get():
                if event == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    # Condições para manter a cobra na tela
    if x > largura:
        x = 0
    if x < 0:
        x = largura
    if y > altura:
        y = 0
    if y < 0:
        y = altura

    # Condição para manter a cobra com tamnho fixo
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450, 40))

    pygame.display.update()
