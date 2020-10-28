"""Gaussian Walker from Khan Academy's course on Natural Simulations"""
from collections import deque
import random

import pygame

from helpers.game import init_game
from helpers.mathematics import monte_carlo


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

NUM_CIRCLES = 10
FRAME_RATE = 30

WIDTH = 600
HEIGHT = 600


if __name__ == '__main__':
    screen = init_game(WIDTH, HEIGHT)
    screen.fill(WHITE)

    clock = pygame.time.Clock()

    step = WIDTH // NUM_CIRCLES
    for i in range(NUM_CIRCLES):
        num = monte_carlo()
        print(num)
        radius = int(num * 30)
        position = (i * step, HEIGHT // 2)
        pygame.draw.circle(screen, BLACK, position, radius, 1)
        pygame.display.flip()
        clock.tick(FRAME_RATE)

    running = True
    while running:
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FRAME_RATE)

    pygame.quit()
