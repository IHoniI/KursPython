import pygame

# INITIALIZE THE GAME
pygame.init()
size = (width, height) = (400, 300)   # rozmiary okna w pikselach
screen = pygame.display.set_mode(size)   # stworzenie display Surface
pygame.display.set_caption('SuperSnake')

# Kolory
black = (0, 0, 0)
gray = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# CLOCK
FPS = 30
clock = pygame.time.Clock()

# MAIN GAME LOOP
done = False

snake = [(100, 100)]

direction = 'R'
new_direction = 'R'

while not done:
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # QUIT Event
            done = True   # chcemy zakończyć pętlę while;
            # samo 'break' nie wystarczy, bo mamy zagnieżdżoną pętlę

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print("event down dict {}".format(event.__dict__))  # atrybuty button, pos
            position = event.pos  # (x, y)

            #get direction

            x = position[0] - snake[0][0]
            y = position[1] - snake[0][1]

            if x > 0:
                if x > abs(y):
                    new_direction = "R"
                elif y > 0:
                    new_direction = "D"
                else:
                    new_direction = "U"
            else:
                if abs(x) > abs(y):
                    new_direction = "L"
                elif y > 0:
                    new_direction = "D"
                else:
                    new_direction = "U"

            print(new_direction)

    # DRAWING
    screen.fill((0, 0, 0))

    box = pygame.Rect(100, 100, 50, 60)
    pygame.draw.rect(screen, (255, 255, 0), box)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()   # deaktywacja pygame
# dalsze instrukcje programu bez pygame