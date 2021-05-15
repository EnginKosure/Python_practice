# Given three arrays of integers, return the sum of elements that are common in all three arrays.

# For example:


# More examples in the test cases.

def common(a, b, c):
    s1 = set(a)
    s2 = set(b)
    s3 = set(c)
    st1 = s1.intersection(s2)
    res_set = st1.intersection(s3)
    final_list = sum(res_set)
    y = sum(s1.intersection(s2).intersection(s3))
    print(final_list)
    print(y)


# = 5 because 2 & 3 are common in all 3 arrays
common([1, 2, 3], [5, 3, 2], [7, 3, 2])
# common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays
