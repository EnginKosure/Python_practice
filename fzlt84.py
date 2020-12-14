# Write a function that returns the length of the shortest contiguous
# sublist whose sum of all elements strictly exceeds n.
def min_length(l, n):
    x = [len(k) if sum(k) > n else -1 for k in [l[i:i+j]
                                                for i in range(0, len(l)) for j in range(1, len(l)-i+1)]]
    if all(i == -1 for i in x):
        return -1
    else:
        return sorted(set(x))[1]


print(min_length([5, 8, 2, -1, 3, 4], 9))  # 2

print(min_length([3, -1, 4, -2, -7, 2], 4))  # 3
# Shortest sublist whose sum exceeds 4 is: [3, -1, 4]

print(min_length([1, 0, 0, 0, 1], 1))  # 5

print(min_length([0, 1, 1, 0], 2))  # -1


def min_length1(lst, n):
    res = sorted([j-i for i in range(len(lst))
                  for j in range(i, len(lst)+1) if sum(lst[i:j]) > n])
    return res[0] if res else -1
