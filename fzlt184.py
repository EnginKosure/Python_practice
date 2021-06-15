from math import ceil
n = 6
print('\n'.join('* ' * i for i in range(1, n + 1)))


def new_avg(arr, newavg):
    next = ceil(newavg * (len(arr) + 1) - sum(arr))
    if next <= 0:
        raise ValueError
    return next
