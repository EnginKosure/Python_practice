def swap(a, b, c):
    print(a+b-c)
    return a + b - c


def swap1(a, b, c):
    print(a ^ b ^ c)
    return a ^ b ^ c


swap(1, 0, 0)  # 1
# a = 1, b = 0, c = b
# return a

swap1(1, 3, 1)  # 3
# a = 1, b = 3, c = a
# return b

swap(27, 31, 31)  # 27
# a = 27, b = 31, c = b
# return a


def swap2(a, b, c):
    return b*(a == c) + a*(b == c)
