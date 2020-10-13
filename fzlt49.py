# Implement division of two positive integers without using
# the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.


def div_wod(x, y):
    res = 0
    while y <= x:
        x -= y
        res += 1
    return res


# print(div_wod(11, 20))  # 0
# print(div_wod(13, 3))  # 4


def div_wod1(x, y, res=0):
    if y <= x:
        res += 1
        return div_wod1(x-y, y, res)
    else:
        return res


def div_wod2(x, y, res=0):
    if x < y:
        return res
    else:
        res += 1
        return div_wod1(x-y, y, res)


print(div_wod2(11, 20))  # 0
print(div_wod2(20, 4))  # 5


def d(x, y, res=0, c=1): return res if x < y else d(x-y, y, res+c, c)


print(d(20, 20))  # 1
print(d(24, 4))  # 6

# q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

# ## The Result
# print(q(unsorted))
