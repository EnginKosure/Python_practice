# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
# implement a function rand7() that returns an integer from 1 to 7 (inclusive).

from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    x = 5*(rand5()-1) + rand5() - 1
    return x % 7 + 1 if x < 21 else rand7()


def rand7_v2():
    return (rand5() + rand5() + rand5() + rand5()) % 7+1
