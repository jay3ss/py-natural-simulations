"""Helpers"""
import math


def normal_pdf(x, mu=0.0, sigma=1.0):
    x = (x - mu) / sigma
    return math.exp(-x*x / 2.) / sigma / math.sqrt(2 * math.pi)
