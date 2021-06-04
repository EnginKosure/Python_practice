def not_visible_cubes(n):
    return (n - 2) ** 3 if n > 2 else 0


def not_visible_cubes1(n):
    return max(n - 2, 0) ** 3


def not_visible_cubes2(n):
    return n > 2 and (n-2)**3
