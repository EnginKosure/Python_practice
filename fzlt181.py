def cut_the_ropes(arr):
    res = [len(arr)]
    arr = sorted(arr)
    while len(set(arr)) > 1:
        arr = list(filter(bool, map(lambda x: x - arr[0], arr)))
        res.append(len(arr))
    return res


# The == operator compares the value or equality of two objects,
# whereas the Python is operator checks whether two variables
# point to the same object in memory.
# Note: In the vast majority of cases you should use the
# equality operators == and !=, except when you’re comparing to None.
a = [1, 2, 3]
b = a

a is b
# True
a == b
# True

c = list(a)

a == c
# True
a is c
# False
