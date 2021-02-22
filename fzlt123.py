# Create a function that takes the side n of the game screen and returns the number of times the snake can eat
# before it runs out of space in the game screen.
from math import floor, log2


def snakefill(n):
    return len(bin(n**2))-3


snakefill(3)  # 3

snakefill(6)  # 5

snakefill(24)  # 9


def snakefill2(n):
    return floor(log2(n*n))
