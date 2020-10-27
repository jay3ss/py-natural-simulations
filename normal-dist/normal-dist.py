import random

import pygame


BLACK = (0, 0, 0)
PURPLE = (214, 159, 214, 10)
WHITE = (255, 255, 255)

RADIUS = 5

WIDTH = 600
HEIGHT = 600
FRAME_RATE = 30


def draw(screen):
     mean = WIDTH / 2
     std_dev = 60

     x = int(random.gauss(mean, std_dev))
     rect = (x, mean, 10, 60)
     pygame.draw.ellipse(screen, PURPLE, rect, 1)


def init_game():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    return screen


if __name__ == '__main__':
    random.seed(1)
    screen = init_game()
    clock = pygame.time.Clock()

    running = True

    screen.fill(WHITE)
    while running:
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw(screen)
        pygame.display.flip()
        clock.tick(FRAME_RATE)

    pygame.quit()
