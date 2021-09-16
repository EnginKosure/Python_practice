def sum_cubes(n):
    result = 0
    if n > 0:
        for i in range(n+1):
            result += i * i * i
    return result


def sum_cubes1(n):
    return sum(i**3 for i in range(0, n+1))


def halving_sum(n):
    return n + halving_sum(n // 2) if n else 0
