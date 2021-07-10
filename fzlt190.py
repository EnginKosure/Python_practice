from math import sqrt
from itertools import count, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


def minimum_number(numbers):
    i = 0
    while True:
        sm = sum(numbers)
        if is_prime(sm + i):
            return i
        i += 1


def is_sator_square(tablet):
    return tablet == [t[::-1] for t in tablet][::-1] == list(map(list, zip(*tablet)))
