"""Game-related helpers"""
import pygame


def init_game(width, height):
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    return screen
