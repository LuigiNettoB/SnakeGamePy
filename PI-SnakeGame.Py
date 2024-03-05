# IMPORTAÇÃO DE BIBLIOTECAS
import pygame , random , sys , time
from pygame.locals import *

# INICIO DO PYGAME 
pygame.init()

# GERAÇÃO ALEATÓRIA DA MAÇÃ
def on_grid_random():
    x = random.randint(0,1180)
    y = random.randint(0,980)
    return (x//20 * 20, y//20 * 20)

# FUNÇÃO DE COLISÃO
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# DEFINIÇÃO DAS DIREÇÕES
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# CONFIGURAÇÃO E ABERTURA DA JANELA
altura= 1000
largura=1200
screen = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake GamePy') # NOME DA JANELA (JOGO)

# CONFIGURAÇÃO DA COBRA
snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((20,20))
snake_skin.fill((0, 51, 153))

# CONFIGURAÇÃO DA MAÇA
apple_pos = on_grid_random()
apple = pygame.Surface((20,20))
apple.fill((255,0,0))

# DIREÇÃO DE INÍCIO
my_direction = LEFT

# FUNÇÃO DE PONTUAÇÃO
def show_score(score):
    font = pygame.font.SysFont('Arial', 30)
    score_text = font.render(f"Pontuação: {score}", True, (0,0,0))
    screen.blit(score_text, (30, 10))

# TEMPO DE EXECUÇÃO DDO JOGO
clock = pygame.time.Clock()


# VARIÁVEIS CONTAGEM REGRESSIVA E PONTUAÇÃO
countdown_start_time = time.time()
countdown_duration = 300
score = 0

# LOOP INFINITO
while True:
    clock.tick(14)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
# EVENTOS DO TECLADO
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
# COLISÃO DA COBRA COM A MAÇÃ
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score +=1

# MENSAGEM DE VITÓRIA AO ATINGIR 10 MAÇÃS CONSUMIDAS
    if score >= 10:
            print("Parabéns! Você venceu!")
            victory_message = font.render("Parabéns! Você venceu!", True, (0,0,0))
            screen.blit(victory_message, (largura // 2 - 150, altura // 2))
            pygame.display.flip()
            pygame.time.wait(3000)  # Aguarda 3 segundos
            pygame.quit()
            sys.exit()


# MOVIMENTAÇÃO DA COBRA
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 20)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 20)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 20, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 20, snake[0][1])

    screen.fill((51, 204, 51))
    screen.blit(apple, apple_pos)
    show_score(score)


# CONTAGEM REGRESSIVA 
    elapsed_time = int(time.time() - countdown_start_time)
    remaining_time = max(0, countdown_duration - elapsed_time)
    font = pygame.font.SysFont('Arial', 30)
    countdown_text = font.render(f"Tempo: {remaining_time // 60:02d}:{remaining_time % 60:02d}", True, (0,0,0))
    screen.blit(countdown_text, (770, 10))
    
    for pos in snake:
        screen.blit(snake_skin,pos)
# ATUALIZAÇÃO DA TELA (JOGO)
    pygame.display.flip()
