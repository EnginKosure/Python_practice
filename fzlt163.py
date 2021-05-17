# Given three arrays of integers, return the sum of elements that are common in all three arrays.


def common(a, b, c):
    out = [x for x in a if x in b and x in c]
    print(sum(out))
    return sum(set(a).intersection(set(b), set(c)))


# = 5 because 2 & 3 are common in all 3 arrays
# common([1, 2, 3], [5, 3, 2], [7, 3, 2])
print(common([1, 2, 3], [5, 3, 2], [7, 3, 2]))
# = 7 because 2,2 & 3 are common in the 3 arrays
common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2])
