"""Game-related helpers"""
import pygame


def init_game(width, height):
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    return screen


def is_in_bounds(position, bounds):
    x, y = position
    w, h = bounds

    return 0 <= x  <= w or 0 <= y <= h

