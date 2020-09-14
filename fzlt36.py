# daily-python-challenge
# What if, instead of being able to climb 1 or 2 steps at a time,
#  you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(staircase(n - x, X) for x in X)
