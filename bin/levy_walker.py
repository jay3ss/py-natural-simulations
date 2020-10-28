"""Lévy Walker from Khan Academy's course on Natural Simulations"""
import random

import pygame

from classes import Walker
from helpers.game import init_game
from helpers.mathematics import monte_carlo


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RADIUS = 3

WIDTH = 600
HEIGHT = 600
FRAME_RATE = 30

BUFFER_LENGTH = 50


def display(screen, walker):
    position = (int(walker.x), int(walker.y))
    pygame.draw.circle(screen, BLACK, position, RADIUS, 1)


def draw_circle(screen, walker):
    walker.walk()
    display(screen, walker)


def draw_lines(screen, points):
    if len(points) > 1:
        points_list = list(points)
        pygame.draw.lines(screen, BLACK, False, points_list)


def levy_walker_update():
    test_func = lambda a, b: a > b
    step_size = random.uniform(monte_carlo(test_func), 10 * monte_carlo(test_func))

    dx = random.uniform(-step_size, step_size)
    dy = random.uniform(-step_size, step_size)

    return dx, dy


if __name__ == '__main__':
    screen = init_game(WIDTH, HEIGHT)
    walker = Walker(WIDTH, HEIGHT, RADIUS, levy_walker_update)
    clock = pygame.time.Clock()

    running = True

    screen.fill(WHITE)
    while running:
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_circle(screen, walker)
        pygame.display.flip()
        clock.tick(FRAME_RATE)

    pygame.quit()
