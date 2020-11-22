import pygame
import random
import sys

pygame.init()
WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (11,238,207)

player_size = 50
player_position = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_position = [random.randint(0,WIDTH - enemy_size), 0]
enemy_list = [enemy_position]

SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0

clock = pygame.time.Clock()
my_font = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
    if score < 20:
        SPEED = 8
    elif score < 40:
        SPEED = 10
    elif score < 60:
        SPEED = 12
    else:
        SPEED = 15 
    return SPEED                   

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_position in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_position[0], enemy_position[1], enemy_size, enemy_size), )

def update_enemy_positions(enemy_list, score):
    for idx, enemy_position in enumerate(enemy_list):
        if enemy_position[1] >= 0 and enemy_position[1] < HEIGHT:
            enemy_position[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score            

def collision_check(enemy_list, player_position):
    for enemy_position in enemy_list:
        if detect_collision(player_position, enemy_position):
            return True
    return False

def detect_collision(player_position, enemy_position):
    p_x = player_position[0]
    p_y = player_position[1]

    e_x = enemy_position[0]
    e_y = enemy_position[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= p_y and p_y < (e_y + enemy_size)):
            return True
    return False            

while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_position[0]
            y = player_position[1]

            if event.key == pygame.K_LEFT:
                x -= 25
            elif event.key == pygame.K_RIGHT:
                x += 25

            player_position = [x,y]                

    screen.fill(BACKGROUND_COLOR)

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    SPEED = set_level(score, SPEED)

    text = "Score:" + str(score)
    label = my_font.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH-200, HEIGHT-40))

    if collision_check(enemy_list, player_position):
        game_over = True
        break

    draw_enemies(enemy_list)

    pygame.draw.rect(screen, RED , (player_position[0], player_position[1] ,player_size ,player_size))

    clock.tick(30)

    pygame.display.update()
