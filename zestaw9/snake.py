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


while not done:
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # QUIT Event
            done = True   # chcemy zakończyć pętlę while;
            # samo 'break' nie wystarczy, bo mamy zagnieżdżoną pętlę
    # DRAWING
    # Rysowanie różnych obiektów, sprawdzanie przekrywania, itp.
       # przerysowanie całego okna z bufora na ekran

    pygame.draw.rect(screen, (255, 0, 0), snake)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()   # deaktywacja pygame
# dalsze instrukcje programu bez pygame