import random

# Method #1: Using an algorithm based on sequencing


def randomOddNumber(a, b):
    a = a // 2
    b = b // 2 - 1
    number = random.randint(a, b)
    number = (number * 2) + 1
    return number


oddNumber = randomOddNumber(0, 100)
print(oddNumber)
