# Implement division of two positive integers without using
# the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.


def div_wod(x, y):
    res = 0
    while y <= x:
        x -= y
        res += 1
    return res


print(div_wod(11, 20))  # 0
print(div_wod(13, 3))  # 4
