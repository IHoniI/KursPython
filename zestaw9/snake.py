import pygame

# INITIALIZE THE GAME
pygame.init()
size = (width, height) = (400, 300)  # rozmiary okna w pikselach
screen = pygame.display.set_mode(size)  # stworzenie display Surface
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

direction = (2, 0)
new_direction = (2, 0)

head = pygame.Rect(100, 100, 10, 10)

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
                    new_direction = (2, 0)  # Right
                elif y > 0:
                    new_direction = (0, 2)  # Up
                else:
                    new_direction = (0, -2)  # Down
            else:
                if abs(x) > abs(y):
                    new_direction = (-2, 0)  # Left
                elif y > 0:
                    new_direction = (0, 2)  # Up
                else:
                    new_direction = (0, -2)  # Down

            if direction[0] + new_direction[0] == 0 and direction[1] + new_direction[1] == 0:
                print("Zabroniony jest ruch wstecz (koniec gry")

            direction = new_direction
            print(new_direction)

    # DRAWING
    screen.fill((0, 0, 0))

    head.move_ip(direction)

    pygame.draw.rect(screen, green, head)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()  # deaktywacja pygame
# dalsze instrukcje programu bez pygame
