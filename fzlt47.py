# This is an interview question asked by Facebook.
# Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
# using only mathematical or bit operations. You can assume b can only be 1 or 0.


def check(x, y, b):
    return x*b | y*(1-b)


def check2(x, y, b):
    return x*b+y*(1-b)


print(check(1, 2, 0))  # 2
print(check(1, 2, 1))  # 1

print(check2(1, 2, 0))  # 2
print(check2(1, 2, 1))  # 1
