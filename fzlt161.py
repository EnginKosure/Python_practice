import math


def solve(p):
    numbers = []
    for i in range(1, int(math.sqrt(p)) + 1):
        if (p - 1) % i == 0:
            numbers.append(i)
            numbers.append((p - 1) // i)
    for i in sorted(numbers):
        if pow(10, i, p) == 1:
            return f'{i}-sum'
        elif pow(10, i, p) == p - 1:
            return f'{i}-altsum'
