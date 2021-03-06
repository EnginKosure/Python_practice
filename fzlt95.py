# Starting with either 3 or 5 and given these operations:

# add 5
# multiply by 3
# You should say if it is possible to reach the target number n.
# def d(x, y, res=0, c=1): return res if x < y else d(x-y, y, res+c, c) #49
def only_5_and_3(n):
    if n < 3:
        return False
    if n == 3:
        return True
    if n % 5 == 0:
        return True
    return only_5_and_3(n / 3) or only_5_and_3(n - 5)


print(only_5_and_3(14))  # True
# 14 = 3*3 + 5

print(only_5_and_3(25))  # True
# 25 = 5+5+5+5+5

print(only_5_and_3(7))  # False
# There exists no path to the target number 7


def only5and3(n):
    while n >= 0:
        if n != 1 and (n == 0 or log(n, 3).is_integer()):
            return True
        n -= 5
    return False
