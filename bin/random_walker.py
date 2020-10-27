"""Random Walker from Khan Academy's course on Natural Simulations"""
from collections import deque
import random

import pygame

from classes import Walker


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RADIUS = 5

WIDTH = 600
HEIGHT = 600
FRAME_RATE = 30

BUFFER_LENGTH = 50


def display(screen, walker):
    position = (walker.x, walker.y)
    pygame.draw.circle(screen, BLACK, position, RADIUS)


def draw(screen, walker):
    walker.walk()
    display(screen, walker)


def draw_lines(screen, points):
    if len(points) > 1:
        points_list = list(points)
        pygame.draw.lines(screen, BLACK, False, points_list)


def init_game():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    return screen


def rand_walker_update():
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)

    return dx, dy


if __name__ == '__main__':
    screen = init_game()
    walker = Walker(WIDTH, HEIGHT, RADIUS, rand_walker_update)
    clock = pygame.time.Clock()

    points = deque(maxlen=BUFFER_LENGTH)

    running = True

    while running:
        screen.fill(WHITE)
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        points.appendleft((walker.x, walker.y))
        draw(screen, walker)
        draw_lines(screen, points)
        pygame.display.flip()
        clock.tick(FRAME_RATE)

    pygame.quit()
