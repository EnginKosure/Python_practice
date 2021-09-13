def fix_the_meerkat(arr):
    arr.reverse()
    return arr


# N = 12
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
def compute_sum(n):
    s = 0
    for i in range(n+1):
        while i:
            i, remainder = divmod(i, 10)
            s += remainder
    return s


print(compute_sum(12))


def compute_sum2(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))
