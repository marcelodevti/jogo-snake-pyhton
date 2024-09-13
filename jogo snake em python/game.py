import pygame
import time
import random

# Inicializando o Pygame
pygame.init()

# Definindo cores (RGB)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensões da janela do jogo
largura_janela = 800
altura_janela = 600

# Definindo tamanho dos blocos e a velocidade
tamanho_bloco = 20
velocidade = 15

# Definindo o display
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo da Cobrinha")

# Controle de tempo
relogio = pygame.time.Clock()

# Fonte do placar
fonte_placar = pygame.font.SysFont("bahnschrift", 25)
fonte_final = pygame.font.SysFont("comicsansms", 35)

# Função para exibir o placar
def seu_placar(pontos):
    valor = fonte_placar.render("Pontuação: " + str(pontos), True, azul)
    janela.blit(valor, [0, 0])

# Função para desenhar a cobrinha
def nossa_cobrinha(tamanho_bloco, lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(janela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

# Função de mensagem final
def mensagem_final(msg, cor):
    mensagem = fonte_final.render(msg, True, cor)
    janela.blit(mensagem, [largura_janela / 6, altura_janela / 3])

# Função principal do jogo
def jogo():
    game_over = False
    game_close = False

    # Posição inicial da cobrinha
    x_cobra = largura_janela / 2
    y_cobra = altura_janela / 2

    # Mudança de posição
    x_cobra_mudanca = 0
    y_cobra_mudanca = 0

    # Lista para guardar o corpo da cobra e comprimento
    lista_cobra = []
    comprimento_cobra = 1

    # Posição da comida
    x_comida = round(random.randrange(0, largura_janela - tamanho_bloco) / 20.0) * 20.0
    y_comida = round(random.randrange(0, altura_janela - tamanho_bloco) / 20.0) * 20.0

    while not game_over:

        while game_close:
            janela.fill(preto)
            mensagem_final("Você perdeu! Pressione Q para sair ou C para continuar", vermelho)
            seu_placar(comprimento_cobra - 1)
            pygame.display.update()

            # Verifica se o jogador deseja sair ou reiniciar
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        # Captura eventos (teclas de movimento)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cobra_mudanca = -tamanho_bloco
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_cobra_mudanca = tamanho_bloco
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_cobra_mudanca = -tamanho_bloco
                    x_cobra_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_cobra_mudanca = tamanho_bloco
                    x_cobra_mudanca = 0

        # Atualizando a posição da cobrinha
        if x_cobra >= largura_janela or x_cobra < 0 or y_cobra >= altura_janela or y_cobra < 0:
            game_close = True
        x_cobra += x_cobra_mudanca
        y_cobra += y_cobra_mudanca
        janela.fill(preto)

        # Desenhando a comida
        pygame.draw.rect(janela, azul, [x_comida, y_comida, tamanho_bloco, tamanho_bloco])

        # Atualizando a posição da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x_cobra)
        cabeca_cobra.append(y_cobra)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verifica se a cobrinha colide consigo mesma
        for bloco in lista_cobra[:-1]:
            if bloco == cabeca_cobra:
                game_close = True

        nossa_cobrinha(tamanho_bloco, lista_cobra)
        seu_placar(comprimento_cobra - 1)

        pygame.display.update()

        # Verifica se a cobrinha comeu a comida
        if x_cobra == x_comida and y_cobra == y_comida:
            x_comida = round(random.randrange(0, largura_janela - tamanho_bloco) / 20.0) * 20.0
            y_comida = round(random.randrange(0, altura_janela - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

# Iniciar o jogo
jogo()
