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

#snake = [(100, 100)]

direction = (BLOCK, 0)
new_direction = (BLOCK, 0)

head = pygame.Rect(100, 100, 10, 10)

new_fruit = True
good_fruit = pygame.Rect(-1, -1, 10, 10)


# czcionka
font = pygame.font.SysFont("comicsansms", size=20)


while not done:
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT Event
            done = True  # chcemy zakończyć pętlę while;
            # samo 'break' nie wystarczy, bo mamy zagnieżdżoną pętlę

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("event down dict {}".format(event.__dict__))  # atrybuty button, pos
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
                print("Zabroniony jest ruch wstecz (koniec gry")

            direction = new_direction
            print(new_direction)

    # Spawning fruit
    if new_fruit:
        good_fruit.x = random.randrange(2, width-2, BLOCK)
        good_fruit.y = random.randrange(2, height-2, BLOCK)
        new_fruit = False

    # DRAWING
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, red, good_fruit)
    head.move_ip(direction)

    if head.colliderect(good_fruit):
        score += 1
        FPS += 1
        new_fruit = True

    pygame.draw.rect(screen, green, head)

    text_surf = font.render("Score: {}".format(score), True, white)
    text_rect = text_surf.get_rect(center=(420, 10))
    screen.blit(text_surf, text_rect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()  # deaktywacja pygame
# dalsze instrukcje programu bez pygame
