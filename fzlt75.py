# parallel or not
def are_parallel_lines(l1, l2):
    if(l1[1] != 0 and l2[1] != 0):
        if(l1[0]/l1[1] == l2[0]/l2[1]):
            return True
        else:
            return False
    else:
        if(l1[0] == l2[0] and l1[1] == l2[1]):
            return True
        else:
            return False

# Can be shortened like this:


def lines_are_parallel(l1, l2):
    return l1[0:2] == l2[0:2] or l1[0]/l2[0] == l1[1]/l2[1]


print(are_parallel_lines([1, 2, 3], [1, 2, 4]))  # ➞ True
# x+2y=3 and x+2y=4 are parallel.

print(are_parallel_lines([2, 4, 1], [4, 2, 1]))  # ➞ False
# 2x+4y=1 and 4x+2y=1 are not parallel.

print(are_parallel_lines([0, 1, 5], [0, 1, 5]))  # ➞ True
# Lines are parallel to themselves.
