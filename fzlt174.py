def solve(a):
    return [int(i/3) if i % 3 == 0 else i*2 for i in a]


print(solve([12, 3, 9, 4, 6, 8]))  # [4, 1, 3, 8, 2, 16]
