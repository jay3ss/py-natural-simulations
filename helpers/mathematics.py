"""Helpers"""
import math
import random


def normal_pdf(x, mu=0.0, sigma=1.0):
    x = (x - mu) / sigma
    return math.exp(-x*x / 2.) / sigma / math.sqrt(2 * math.pi)


def monte_carlo(test_func=None):
    """Generate random numbers, but prefer higher numbers."""

    if test_func is None:
        test_func = lambda a, b: a < b

    while True:
        rand1 = random.random()
        rand2 = random.random()
        probability = rand1

        if test_func(rand2, probability):
            return rand1
