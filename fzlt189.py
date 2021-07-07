import math


def close_compare(a, b, margin=0):
    if margin >= abs(a - b) or a == b:
        return 0
    elif a < b:
        return -1
    return 1


def close_compare1(a, b, margin=0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1


def circle_diameter(sides, side_length):
    return side_length / math.tan(math.pi / sides)
