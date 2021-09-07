# Return a new array consisting of elements which are multiple of their own index
# in input array (length > 1).

# Some cases:

# [22, -6, 32, 82, 9, 25] => [-6, 32, 25]

# [68, -1, 1, -7, 10, 10] => [-1, 10]

# [-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]
def multiple_of_index(arr):
    return [e for i, e in enumerate(arr) if (i != 0) and (e % i == 0)]
    # return [e for i, e in enumerate(arr) if i and not e % i]


print(multiple_of_index([68, 1, -7, 10, 10, 10]))
print(multiple_of_index([22, -6, 32, 82, 9, 25]))
print(multiple_of_index([-56, -85, 72, -26, -14, 76, -
                         27, 72, 35, -21, -67, 87, 0, 21, 59, 27, -92, 68]))


def multiple_of_index1(l):
    return [l[i] for i in range(1, len(l)) if l[i] % i == 0]
