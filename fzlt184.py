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
