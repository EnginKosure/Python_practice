def fix_the_meerkat(arr):
    arr.reverse()
    return arr


# N = 12
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
def compute_sum(n):
    return sum([i if i < 10 else (i//10+i % 10) for i in range(n+1)])


print(compute_sum(12))
