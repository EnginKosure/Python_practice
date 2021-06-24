import re
from math import ceil
n = 6
print('\n'.join('* ' * i for i in range(1, n + 1)))


def new_avg(arr, newavg):
    next = ceil(newavg * (len(arr) + 1) - sum(arr))
    if next <= 0:
        raise ValueError
    return next


len(re.findall('python', 'python is a programming language. python is python.'))


def bonus(arr, s):
    bonus = s / sum(1 / x for x in arr)
    return [round(bonus / x) for x in arr]


def order_food(lst):
    keys = [x['meal'] for _, x in enumerate(lst)]
    return {key: keys.count(key) for key in keys}


def largest_pair_sum(numbers):
    return sum(sorted(numbers, reverse=True)[:2])


def find_outlier(integers):
    mods = [n % 2 for n in integers]
    return integers[mods.index(0)] if sum(mods[:3]) > 1 else integers[mods.index(1)]


def chess_knight(cell):
    x, y = ord(cell[0]) - ord('a') + 1, int(cell[1])
    moves = {(-2, -1), (-2, 1), (-1, 2), (1, 2),
             (2, 1), (2, -1), (1, -2), (-1, -2)}
    return sum(0 < x + i < 9 and 0 < y + j < 9 for i, j in moves)


def add_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Input arguments are not of equal length")
    return [array1[i] + array2[i] for i in range(len(array1))]
