import time

import pygame
import random

# INITIALIZE THE GAME
pygame.init()
size = (width, height) = (500, 400)  # rozmiary okna w pikselach
screen = pygame.display.set_mode(size)  # stworzenie display Surface
pygame.display.set_caption('SuperSnake')

BLOCK = 10
score = 0

# Kolory
black = (0, 0, 0)
gray = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# CLOCK
FPS = 20
clock = pygame.time.Clock()

# MAIN GAME LOOP
done = False

snake = [(90, 100)]

direction = (BLOCK, 0)
new_direction = (BLOCK, 0)

head = pygame.Rect(100, 100, 10, 10)

new_fruit = True
good_fruit = pygame.Rect(-1, -1, 10, 10)


# czcionki
font = pygame.font.SysFont("comicsansms", size=20)
font2 = pygame.font.SysFont("comicsansms", size=40)


def game_over(reason):
    screen.fill((0, 0, 0))
    text_surf1 = font2.render("GAME OVER!", True, red)
    text_rect1 = text_surf1.get_rect(center=(width // 2, (height // 2) - 10))
    screen.blit(text_surf1, text_rect1)

    text_surf = font.render(reason, True, red)
    text_rect = text_surf.get_rect(center=(width // 2, (height // 2) + 40))
    screen.blit(text_surf, text_rect)

    text_surf = font.render("score: {}".format(score), True, red)
    text_rect = text_surf.get_rect(center=(width // 2, (height // 2) + 70))
    screen.blit(text_surf, text_rect)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()


while not done:
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos  # (x, y)

            # get direction
            x = position[0] - head.x
            y = position[1] - head.y

            if x > 0:
                if x > abs(y):
                    new_direction = (BLOCK, 0)  # Right
                elif y > 0:
                    new_direction = (0, BLOCK)  # Up
                else:
                    new_direction = (0, -BLOCK)  # Down
            else:
                if abs(x) > abs(y):
                    new_direction = (-BLOCK, 0)  # Left
                elif y > 0:
                    new_direction = (0, BLOCK)  # Up
                else:
                    new_direction = (0, -BLOCK)  # Down

            if direction[0] + new_direction[0] == 0 and direction[1] + new_direction[1] == 0:
                game_over("Illegal move")

            direction = new_direction

    # Spawning fruit
    if new_fruit:
        good_fruit.x = random.randrange(10, width-10, BLOCK)
        good_fruit.y = random.randrange(10, height-10, BLOCK)
        new_fruit = False

    # DRAWING
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, red, good_fruit)

    new_head = (head.x + direction[0], head.y + direction[1])
    snake.insert(0, new_head)

    head.x, head.y = new_head
    if not head.colliderect(good_fruit):
        snake.pop()
    # jeśli zjadłem owoc nie usuwam ogona
    else:
        score += 1
        FPS += 1
        new_fruit = True

    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], BLOCK, BLOCK))

    if head.left < 0 or head.right > width or head.top < 0 or head.bottom > height:
        game_over("Snake outside the board")

    text_surf = font.render("Score: {}".format(score), True, white)
    text_rect = text_surf.get_rect(center=(420, 10))
    screen.blit(text_surf, text_rect)

    pygame.display.flip()

    clock.tick(FPS)
