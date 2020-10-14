# Given an integer n and a list of integers,
# write a function that randomly generates a number
# from 0 to n-1 that isn't in that given integer list.
from random import choice


def random_int(n, l):
    return choice([i for i in range(n) if i not in l])
